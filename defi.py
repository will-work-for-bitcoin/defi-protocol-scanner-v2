#!/usr/bin/env python3
"""
DeFi Protocol Scanner - Analyze DeFi protocol health metrics
Fetches TVL, volume, and security scores from DefiLlama

BTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9
"""
import json
import urllib.request
import sys
from datetime import datetime

def fetch_tvl_data():
    """Fetch TVL data from DefiLlama"""
    url = "https://api.llama.fi/protocols"
    req = urllib.request.Request(url, headers={'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.loads(response.read())

def display_protocols(protocols, limit=20):
    """Display protocol analysis"""
    print("=" * 70)
    print("DEFI PROTOCOL SCANNER")
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    sorted_protos = sorted(protocols, key=lambda x: x.get('tvl', 0), reverse=True)
    
    print(f"\n{'Protocol':<20} {'TVL':>12} {'Chain':<15} {'Category':<15}")
    print("-" * 65)
    
    for proto in sorted_protos[:limit]:
        name = proto.get('name', 'Unknown')[:19]
        tvl = proto.get('tvl', 0)
        chain = proto.get('chain', 'Unknown')[:14]
        category = proto.get('category', 'Unknown')[:14]
        
        if tvl >= 1e9:
            tvl_str = f"${tvl/1e9:,.2f}B"
        elif tvl >= 1e6:
            tvl_str = f"${tvl/1e6:,.1f}M"
        else:
            tvl_str = f"${tvl:,.0f}"
        
        print(f"{name:<20} {tvl_str:>12} {chain:<15} {category:<15}")
    
    print(f"\nBTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9")

def main():
    try:
        protocols = fetch_tvl_data()
        display_protocols(protocols, 20)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
