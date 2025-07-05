import re
from urllib.parse import urlparse

def print_banner():
    banner = r"""
 '##:::::::'####:'##::: ##:'##:::'##:::::::::::::::::::::::::::::::
 ##:::::::. ##:: ###:: ##: ##::'##::::::::::::::::::::::::::::::::
 ##:::::::: ##:: ####: ##: ##:'##:::::::::::::::::::::::::::::::::
 ##:::::::: ##:: ## ## ##: #####::::::::::::::::::::::::::::::::::
 ##:::::::: ##:: ##. ####: ##. ##:::::::::::::::::::::::::::::::::
 ##:::::::: ##:: ##:. ###: ##:. ##::::::::::::::::::::::::::::::::
 ########:'####: ##::. ##: ##::. ##:::::::::::::::::::::::::::::::
........::....::..::::..::..::::..::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::'##:::::'##:'####::'######::'########: 
::::::::::::::::::::::::::: ##:'##: ##:. ##::'##... ##: ##.....:: 
::::::::::::::::::::::::::: ##: ##: ##:: ##:: ##:::..:: ##::::::: 
::::::::::::::::::::::::::: ##: ##: ##:: ##::. ######:: ######::: 
::::::::::::::::::::::::::: ##: ##: ##:: ##:::..... ##: ##...:::: 
::::::::::::::::::::::::::: ##: ##: ##:: ##::'##::: ##: ##::::::: 
:::::::::::::::::::::::::::. ###. ###::'####:. ######:: ########: 
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    🛡️
    Wisely check your links, surf with confidence.
    """
    print(banner)

def is_suspicious(url):
    issues = []

    try:
        parsed = urlparse(url)

        # Rule 1: HTTPS check
        if parsed.scheme != "https":
            issues.append("🔒 Does not use HTTPS")

        # Rule 2: Suspicious characters in domain
        if "@" in parsed.netloc or "%" in parsed.netloc:
            issues.append("❗ Domain contains suspicious characters (@, %)")

        # Rule 3: URL too long
        if len(url) > 100:
            issues.append("📏 URL is very long")

        # Rule 4: Suspicious keywords
        suspicious_keywords = ["login", "verify", "update", "secure", "account", "bank"]
        for word in suspicious_keywords:
            if word in url.lower():
                issues.append(f"⚠️ Contains suspicious keyword: '{word}'")

        # Rule 5: IP address usage
        if re.match(r'^(https?:\/\/)?(\d{1,3}\.){3}\d{1,3}', url):
            issues.append("🧠 Uses IP address instead of domain")

        return issues
    except Exception as e:
        return ["❌ Invalid URL format"]

def main():
    print_banner()
    url = input("🔗 Enter a URL to check: ").strip()
    
    if not url:
        print("❗ Please enter a URL.")
        return

    issues = is_suspicious(url)

    if "❌ Invalid URL format" in issues:
        print("❌ Invalid URL format.")
    elif issues:
        print("\n🔴 Suspicious URL detected!")
        print("Reasons:")
        for issue in issues:
            print("•", issue)
    else:
        print("\n✅ This URL looks safe!")

if __name__ == "__main__":
    main()
