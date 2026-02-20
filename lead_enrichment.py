#!/usr/bin/env python3
"""
RE Lead Enrichment Tool
Enriches real estate leads with phone numbers and property data.
"""
import csv
import json
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Optional
import time

VERSION = "1.0.0"

class LeadEnricher:
    def __init__(self, input_file: str, output_file: str, license_key: Optional[str] = None):
        self.input_file = input_file
        self.output_file = output_file
        self.license_key = license_key
        self.progress_file = f"{input_file}.progress.json"
        self.is_pro = self._validate_license(license_key)
        
    def _validate_license(self, key: Optional[str]) -> bool:
        """Validate license key. Pro tier unlocks batch processing."""
        if not key:
            return False
        # Simple validation - in production, check against server
        return len(key) == 32 and key.startswith("REPRO-")
    
    def load_progress(self) -> Dict:
        """Load processing progress."""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {
            'processed': 0,
            'enriched': 0,
            'failed': 0,
            'results': {}
        }
    
    def save_progress(self, progress: Dict):
        """Save processing progress."""
        with open(self.progress_file, 'w') as f:
            json.dump(progress, f, indent=2)
    
    def load_leads(self) -> List[Dict]:
        """Load leads from CSV."""
        leads = []
        with open(self.input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                leads.append(row)
        return leads
    
    def save_results(self, leads: List[Dict], progress: Dict):
        """Save enriched leads to output CSV."""
        if not leads:
            return
        
        # Add enrichment columns
        fieldnames = list(leads[0].keys())
        if 'Phone' not in fieldnames:
            fieldnames.append('Phone')
        if 'Email' not in fieldnames:
            fieldnames.append('Email')
        if 'Enrichment_Status' not in fieldnames:
            fieldnames.append('Enrichment_Status')
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for lead in leads:
                row = dict(lead)
                lead_id = self._get_lead_id(lead)
                
                if lead_id in progress['results']:
                    result = progress['results'][lead_id]
                    row['Phone'] = result.get('phone', '')
                    row['Email'] = result.get('email', '')
                    row['Enrichment_Status'] = result.get('status', 'pending')
                else:
                    row['Phone'] = ''
                    row['Email'] = ''
                    row['Enrichment_Status'] = 'pending'
                
                writer.writerow(row)
    
    def _get_lead_id(self, lead: Dict) -> str:
        """Generate unique ID for lead."""
        # Support multiple column name variations
        name = (lead.get('Name') or 
                lead.get('full_name') or 
                lead.get('Owner_Name') or 
                f"{lead.get('first_name', '')} {lead.get('last_name', '')}".strip())
        address = (lead.get('Address') or 
                   lead.get('address') or 
                   lead.get('Property_Address') or 
                   lead.get('Mailing_Address') or '')
        return f"{name}|{address}".strip()
    
    def extract_phone(self, text: str) -> Optional[str]:
        """Extract and normalize phone number from text."""
        patterns = [
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                digits = re.sub(r'\D', '', match.group())
                if len(digits) == 10:
                    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return None
    
    def enrich_lead_manual(self, lead: Dict) -> Dict:
        """
        Manual enrichment mode - generates search query for user.
        In Pro mode, this would be automated via browser automation.
        """
        # Support multiple column name variations
        name = (lead.get('Name') or 
                lead.get('full_name') or 
                lead.get('Owner_Name') or 
                f"{lead.get('first_name', '')} {lead.get('last_name', '')}".strip())
        city = lead.get('City') or lead.get('city') or ''
        state = lead.get('State') or lead.get('State_Abbr') or lead.get('state') or 'FL'
        
        search_query = f'"{name}" {city} {state} phone'
        
        print(f"\n🔍 Search Query: {search_query}")
        print("   Visit: https://www.truepeoplesearch.com")
        print("   Or try: https://www.fastpeoplesearch.com")
        
        phone = input("   Enter phone number (or press Enter to skip): ").strip()
        email = input("   Enter email (or press Enter to skip): ").strip()
        
        return {
            'phone': self.extract_phone(phone) if phone else '',
            'email': email,
            'status': 'manual_enriched' if (phone or email) else 'skipped'
        }
    
    def enrich_batch(self, leads: List[Dict], progress: Dict) -> Dict:
        """
        Batch enrichment (Pro feature).
        For MVP, this is a placeholder for automated browser lookups.
        """
        if not self.is_pro:
            print("\n⚠️  Batch processing requires a Pro license ($49)")
            print("   Visit: [PRODUCT_URL] to upgrade")
            sys.exit(1)
        
        print("\n🚀 Pro Mode: Automated batch processing")
        print("   This feature uses browser automation to lookup leads automatically.")
        print("   Estimated time: ~20-30 seconds per lead")
        
        # TODO: Implement browser automation via Playwright/Selenium
        # For now, show what would happen
        remaining = len(leads) - progress['processed']
        print(f"\n   {remaining} leads remaining to process")
        print("   [Browser automation would run here in production]")
        
        return progress
    
    def run(self, batch: bool = False):
        """Run the enrichment process."""
        print(f"\n📋 RE Lead Enrichment Tool v{VERSION}")
        print(f"   Mode: {'Pro (Batch)' if self.is_pro and batch else 'Free (Manual)'}\n")
        
        leads = self.load_leads()
        progress = self.load_progress()
        
        print(f"✅ Loaded {len(leads)} leads from {self.input_file}")
        print(f"   Already processed: {progress['processed']}")
        print(f"   Enriched: {progress['enriched']}")
        print(f"   Failed: {progress['failed']}\n")
        
        if batch and self.is_pro:
            progress = self.enrich_batch(leads, progress)
        else:
            # Manual mode - process one at a time
            if not self.is_pro:
                print("⚠️  Free tier: Manual lookup (5 per day limit)")
                print("   Upgrade to Pro for automated batch processing\n")
            
            daily_limit = 5 if not self.is_pro else float('inf')
            processed_today = 0
            
            for i, lead in enumerate(leads[progress['processed']:]):
                if processed_today >= daily_limit:
                    print(f"\n⚠️  Daily limit reached ({daily_limit} lookups)")
                    break
                
                lead_id = self._get_lead_id(lead)
                
                if lead_id in progress['results']:
                    continue  # Already processed
                
                print(f"\n[{i+1}/{len(leads)}] {lead_id}")
                result = self.enrich_lead_manual(lead)
                
                progress['results'][lead_id] = result
                progress['processed'] += 1
                
                if result['status'] != 'skipped':
                    progress['enriched'] += 1
                else:
                    progress['failed'] += 1
                
                processed_today += 1
                self.save_progress(progress)
        
        # Save final results
        self.save_results(leads, progress)
        
        print(f"\n✅ Enrichment complete!")
        print(f"   Results saved to: {self.output_file}")
        print(f"   Total enriched: {progress['enriched']}/{len(leads)}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='RE Lead Enrichment Tool - Find phone numbers and emails for your leads'
    )
    parser.add_argument('input', help='Input CSV file with leads')
    parser.add_argument('-o', '--output', help='Output CSV file (default: input_enriched.csv)')
    parser.add_argument('-l', '--license', help='Pro license key for batch processing')
    parser.add_argument('-b', '--batch', action='store_true', help='Batch mode (Pro only)')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {VERSION}')
    
    args = parser.parse_args()
    
    output = args.output or args.input.replace('.csv', '_enriched.csv')
    
    enricher = LeadEnricher(args.input, output, args.license)
    enricher.run(batch=args.batch)

if __name__ == '__main__':
    main()
