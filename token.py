#!/usr/bin/env python3
import requests
import re
import time

print("=" * 60)
print("🔥 FACEBOOK ACCESS TOKEN EXTRACTOR 🔥")
print("📱 WORKING FOR ALL ACCOUNTS 2025")
print("=" * 60)

# Input cookie
cookie = input("
📋 Paste your FULL Facebook Cookie: ").strip()

print("
🔄 Setting up headers...")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.facebook.com/',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

print("
🌐 Scanning ALL endpoints (5 locations)...")
endpoints = [
    "https://business.facebook.com/business_locations",
    "https://www.facebook.com/ads/tools/account_quality",
    "https://business.facebook.com/business/help/170572223145522",
    "https://www.facebook.com/adsmanager/manage",
    "https://business.facebook.com/business_management"
]

all_tokens = []

print("
🔍 Searching tokens...")
for i, url in enumerate(endpoints, 1):
    print(f"  [{i}/5] Checking: {url.split('/')[2]}...")
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=15)
        
        # ALL TOKEN PATTERNS 2025
        patterns = [
            r'EAAD[A-Za-z0-9]{200,}',
            r'EAAG[A-Za-z0-9]{200,}',
            r'EAAU[A-Za-z0-9]{200,}',
            r'EAAB[A-Za-z0-9]{200,}',
            r'EGAB[A-Za-z0-9]{200,}'
        ]
        
        for pattern in patterns:
            tokens = re.findall(pattern, response.text)
            all_tokens.extend(tokens)
            
    except Exception as e:
        print(f"    ❌ Error: {str(e)[:50]}")

# Remove duplicates + sort by length
unique_tokens = list(set([t for t in all_tokens if len(t) > 200]))
unique_tokens.sort(key=len, reverse=True)

print("
" + "=" * 60)
if unique_tokens:
    print("🎉 TOKENS FOUND!")
    print("=" * 60)
    
    for i, token in enumerate(unique_tokens[:3], 1):
        print(f"
  {i}. FULL TOKEN ({len(token)} chars):")
        print(f"     {token}")
        print(f"     📋 Long press → Copy!")
        
        # TEST TOKEN
        print("     🧪 Testing...", end=" ")
        test_url = f"https://graph.facebook.com/v20.0/me?access_token={token}"
        test_response = requests.get(test_url, timeout=10)
        if test_response.status_code == 200:
            try:
                user_data = test_response.json()
                print("✅ WORKING!")
                print(f"     👤 Name: {user_data.get('name', 'Unknown')}")
                print(f"     🆔 ID: {user_data.get('id', 'Unknown')}")
            except:
                print("✅ Valid (parse error)")
        else:
            print("❌ Failed")
    
    print("
💾 SAVING BEST TOKEN...")
    best_token = unique_tokens[0]
    with open("token.txt", "w") as f:
        f.write(best_token)
    print("✅ SAVED → token.txt")
    
else:
    print("❌ No tokens found")
    print("
💡 TIPS:")
    print("   • Use fresh cookie from logged-in browser")
    print("   • Need Business/Page access")
    print("   • Try desktop Chrome cookie")

print("
" + "=" * 60)
print("✅ Ready for Messenger Bot!")
print("🔗 Next: cat token.txt")
