#!/usr/bin/env python3
"""
Browser automation module for RE Lead Enrichment Tool.
Uses OpenClaw's browser control for TruePeopleSearch lookups.
"""
import json
import subprocess
import time
import re
from typing import Dict, Optional

class BrowserAutomation:
    """Handles automated browser-based phone/email lookups."""
    
    def __init__(self, profile='chrome', headless=False):
        """
        Initialize browser automation.
        
        Args:
            profile: Browser profile to use ('chrome' for relay, 'openclaw' for managed)
            headless: Whether to run headless (chrome relay doesn't support this)
        """
        self.profile = profile
        self.headless = headless
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        ]
        
    def _call_browser_tool(self, action: str, **kwargs) -> Dict:
        """
        Call OpenClaw browser tool via JSON API.
        
        Args:
            action: Browser action (open, snapshot, act, etc.)
            **kwargs: Additional parameters for the action
            
        Returns:
            Dict response from browser tool
        """
        cmd = [
            'openclaw', 'tool', 'browser',
            '--action', action,
            '--profile', self.profile
        ]
        
        # Add additional params
        for key, value in kwargs.items():
            if isinstance(value, bool):
                if value:
                    cmd.append(f'--{key}')
            else:
                cmd.extend([f'--{key}', str(value)])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0 and result.stdout:
                return json.loads(result.stdout)
            return {'error': result.stderr or 'Unknown error'}
        except subprocess.TimeoutExpired:
            return {'error': 'Browser command timeout'}
        except json.JSONDecodeError:
            return {'error': 'Invalid JSON response'}
        except Exception as e:
            return {'error': str(e)}
    
    def lookup(self, name: str, city: str, state: str = 'FL', max_retries: int = 3) -> Optional[Dict]:
        """
        Look up contact info for a person.
        
        Args:
            name: Person's full name
            city: City name
            state: State abbreviation (default: FL)
            max_retries: Maximum retry attempts
            
        Returns:
            Dict with 'phone', 'email', 'address' keys, or None on failure
        """
        # Build search URL
        search_url = f"https://www.truepeoplesearch.com/results?name={name.replace(' ', '%20')}&citystatezip={city}%20{state}"
        
        for attempt in range(max_retries):
            try:
                # Open search page
                open_result = self._call_browser_tool('open', targetUrl=search_url)
                if 'error' in open_result:
                    print(f"  ⚠️ Open failed (attempt {attempt+1}/{max_retries}): {open_result['error']}")
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
                
                # Wait for results to load
                time.sleep(3 + (attempt * 2))
                
                # Take snapshot to extract data
                snapshot = self._call_browser_tool('snapshot', snapshotFormat='aria')
                if 'error' in snapshot:
                    print(f"  ⚠️ Snapshot failed (attempt {attempt+1}/{max_retries}): {snapshot['error']}")
                    continue
                
                # Extract contact info from snapshot
                contact_info = self._extract_contact_info(snapshot.get('content', ''))
                
                if contact_info and (contact_info.get('phone') or contact_info.get('email')):
                    return contact_info
                
                print(f"  ⚠️ No contact info found (attempt {attempt+1}/{max_retries})")
                
            except Exception as e:
                print(f"  ⚠️ Lookup error (attempt {attempt+1}/{max_retries}): {str(e)}")
            
            # Delay between retries
            if attempt < max_retries - 1:
                time.sleep(3 + (attempt * 2))
        
        return None
    
    def _extract_contact_info(self, html_content: str) -> Dict:
        """
        Extract phone, email, address from HTML content.
        
        Args:
            html_content: HTML or aria snapshot content
            
        Returns:
            Dict with phone, email, address keys
        """
        info = {
            'phone': '',
            'email': '',
            'address': ''
        }
        
        # Extract phone numbers
        phone_patterns = [
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            r'\d{3}-\d{3}-\d{4}'
        ]
        
        for pattern in phone_patterns:
            matches = re.findall(pattern, html_content)
            if matches:
                # Normalize to (XXX) XXX-XXXX
                phone = matches[0]
                digits = re.sub(r'\D', '', phone)
                if len(digits) == 10:
                    info['phone'] = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
                    break
        
        # Extract email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_matches = re.findall(email_pattern, html_content)
        if email_matches:
            info['email'] = email_matches[0]
        
        # Extract address (simplified - looks for street patterns)
        address_pattern = r'\d+\s+[\w\s]+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Court|Ct|Boulevard|Blvd)'
        address_matches = re.findall(address_pattern, html_content, re.IGNORECASE)
        if address_matches:
            info['address'] = address_matches[0]
        
        return info
    
    def batch_lookup(self, leads: list, delay: float = 5.0, progress_callback=None) -> list:
        """
        Perform batch lookups with rate limiting.
        
        Args:
            leads: List of dicts with 'name', 'city', 'state' keys
            delay: Delay between lookups (seconds)
            progress_callback: Optional callback function(current, total, result)
            
        Returns:
            List of results (same order as input, None for failures)
        """
        results = []
        total = len(leads)
        
        for i, lead in enumerate(leads):
            print(f"\n[{i+1}/{total}] Looking up: {lead['name']}, {lead['city']}, {lead.get('state', 'FL')}")
            
            result = self.lookup(
                name=lead['name'],
                city=lead['city'],
                state=lead.get('state', 'FL')
            )
            
            results.append(result)
            
            if progress_callback:
                progress_callback(i + 1, total, result)
            
            # Rate limiting (except on last item)
            if i < total - 1:
                time.sleep(delay)
        
        return results


if __name__ == '__main__':
    # Test mode
    automation = BrowserAutomation(profile='chrome')
    
    test_lead = {
        'name': 'John Smith',
        'city': 'Orlando',
        'state': 'FL'
    }
    
    print(f"Testing lookup for: {test_lead['name']}, {test_lead['city']}")
    result = automation.lookup(test_lead['name'], test_lead['city'], test_lead['state'])
    
    if result:
        print(f"\n✅ Found:")
        print(f"  Phone: {result.get('phone', 'N/A')}")
        print(f"  Email: {result.get('email', 'N/A')}")
        print(f"  Address: {result.get('address', 'N/A')}")
    else:
        print("\n❌ No results found")
