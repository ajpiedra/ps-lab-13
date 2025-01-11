import json
import random
from datetime import datetime, timedelta

# Function to generate a random timestamp within the given interval
def random_timestamp(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Predefined list of real-world locations (latitude and longitude) with corresponding IPs
real_ips_locations = [
    ("203.0.113.10", "2.3522", "48.8566"),   # France
    ("198.51.100.20", "13.4050", "52.5200"), # Germany
    ("192.0.2.30", "-0.1278", "51.5074"),    # UK
    ("192.168.0.1", "-74.0060", "40.7128"),  # New York, USA
    ("203.0.113.5", "-118.2437", "34.0522"), # Los Angeles, USA
    ("198.51.100.6", "2.3522", "48.8566"),   # Paris, France
    ("192.168.1.2", "139.6917", "35.6895"),  # Tokyo, Japan
    ("203.0.113.11", "151.2093", "-33.8688"),# Sydney, Australia
    ("198.51.100.21", "37.6173", "55.7558"), # Moscow, Russia
    ("192.0.2.31", "-122.4194", "37.7749"),  # San Francisco, USA
    ("198.51.100.17", "4.9041", "52.3676"),  # Amsterdam, Netherlands
    ("192.0.2.19", "-58.3816", "-34.6037"),  # Buenos Aires, Argentina
    ("203.0.113.25", "144.9631", "-37.8136"),# Melbourne, Australia
    ("192.168.1.22", "116.4074", "39.9042"), # Beijing, China
    ("198.51.100.29", "30.0444", "31.2357"), # Cairo, Egypt
    ("203.0.113.31", "151.2073", "-33.8679"),# Sydney, Australia (alt IP)
    ("192.0.2.44", "-0.1276", "51.5074"),    # London, UK
    ("198.51.100.45", "-99.1332", "19.4326"),# Mexico City, Mexico
    ("192.168.1.55", "103.8198", "1.3521"),  # Singapore
    ("203.0.113.65", "151.2148", "-33.8523"),# Sydney, Australia (another alt)
    ("198.51.100.56", "55.2708", "25.2048"),  # Dubai, UAE
    ("192.0.2.69", "-3.7038", "40.4168"),    # Madrid, Spain
    ("203.0.113.77", "-43.1729", "-22.9068"),# Rio de Janeiro, Brazil
    ("198.51.100.88", "-58.3838", "-34.6146"),# Buenos Aires, Argentina (alt IP)
    ("192.168.1.99", "77.1025", "28.7041"),   # New Delhi, India
    ("203.0.113.111", "3.1589", "19.0758"),  # Mumbai, India
    ("198.51.100.123", "74.0060", "40.7128"),# New York, USA (alt IP)
    ("192.0.2.142", "139.6503", "35.6762"),  # Tokyo, Japan (alt IP)
    ("198.51.100.156", "2.2945", "48.8584"), # Paris, France (alt IP)
    ("203.0.113.168", "31.2357", "30.0444")  # Cairo, Egypt (alt IP)
]


# Predefined mappings of IPs to locations for DDoS attacks
ddos_ips_locations = [
    ("203.0.113.10", "2.3522", "48.8566"),  # France
    ("198.51.100.20", "13.4050", "52.5200"),  # Germany
    ("192.0.2.30", "-0.1278", "51.5074")    # UK
]

# Function to generate a log entry
def generate_log_entry(timestamp, ip, user_agent, location, method, url, status_code, referrer, response_time_ms):
    return {
        "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ip": ip,
        "user_agent": user_agent,
        "location": f"POINT({location[1]} {location[0]})",
        "method": method,
        "url": url,
        "status_code": status_code,
        "referrer": referrer,
        "response_time_ms": response_time_ms
    }

# Function to generate logs
def generate_logs(start_time, end_time, ddos_start, ddos_end, num_ddos_entries, num_normal_entries):
    logs = []
    real_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 12; Mobile; rv:98.0) Gecko/98.0 Firefox/98.0",
        "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        ]
    ddos_user_agent = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    methods = ["GET", "POST", "PUT", "DELETE"]
    real_urls = [
        "/courses/python-fundamentals",
        "/courses/aws-certified-solutions-architect",
        "/courses/javascript-essentials",
        "/users/johndoe/profile",
        "/categories/development",
        "/categories/it-ops",
        "/courses/machine-learning",
        "/courses/cloud-computing",
        "/courses/web-development",
        "/courses/data-analysis",
        "/courses/data-science",
        "/courses/devops-foundations",
        "/courses/cyber-security",
        "/courses/full-stack-development",
        "/courses/agile-methodologies",
        "/courses/blockchain-basics",
        "/courses/docker-and-kubernetes",
        "/courses/front-end-development",
        "/courses/backend-development",
        "/users/janedoe/profile",
        "/categories/business",
        "/categories/design",
        "/courses/systems-administration",
        "/courses/project-management",
        "/courses/microsoft-azure",
        "/courses/html-css",
        "/courses/react",
        "/courses/angular",
        "/courses/vue",
        "/courses/sql-databases",
        "/courses/git-and-github",
        "/courses/digital-marketing",
        "/categories/software-development",
        "/categories/cloud-services",
        "/courses/networking-fundamentals",
        "/courses/operating-systems",
        "/courses/linux-essentials",
        "/courses/windows-server",
        "/courses/office-365",
        "/courses/microservices",
        "/courses/c-sharp",
        "/courses/java",
        "/courses/ruby-on-rails",
        "/courses/python-advanced",
        "/courses/aws-advanced"
    ]
    ddos_urls = [
        "/index.html",
        "/categories/it-ops",
        "/courses/machine-learning",
        "/courses/cloud-computing",
        "/"
    ]
    status_codes = [200, 201, 404, 500, 503]
    referrers = [
        "https://www.google.com",
        "https://www.bing.com",
        "https://www.pluralsight.com",
        "https://www.linkedin.com",
        "https://twitter.com",
        "https://facebook.com",
        ""
    ]

    # Generate normal access logs
    for _ in range(num_normal_entries):
        timestamp = random_timestamp(start_time, end_time)
        ip, lon, lat = random.choice(real_ips_locations)
        user_agent = random.choice(real_user_agents)
        location = (lat, lon)
        method = random.choice(methods)
        url = random.choice(real_urls)
        status_code = random.choice(status_codes)
        referrer = random.choice(referrers)
        response_time_ms = random.randint(20, 500),
        logs.append(generate_log_entry(timestamp, ip, user_agent, location, method, url, status_code, referrer, response_time_ms))
    
    # Generate DDoS attack logs from 3 different countries in Europe
    for _ in range(num_ddos_entries):
        timestamp = random_timestamp(ddos_start, ddos_end)
        ip, lon, lat = random.choice(ddos_ips_locations)
        user_agent = ddos_user_agent
        location = (lat, lon)
        method = random.choice(methods)
        url = random.choice(ddos_urls)
        status_code = random.choice([200, 403, 503])  # Mixed status codes for DDoS requests
        referrer = ""
        response_time_ms = random.randint(500, 2000),
        logs.append(generate_log_entry(timestamp, ip, user_agent, location, method, url, status_code, referrer, response_time_ms))
    
    # Sort logs by timestamp
    logs.sort(key=lambda x: x["timestamp"])
    
    return logs

# Parameters
start_time = datetime(2025, 1, 11, 10, 0, 0)
end_time = datetime(2025, 1, 11, 10, 30, 0)
ddos_start = datetime(2025, 1, 11, 10, 7, 0)
ddos_end = datetime(2025, 1, 11, 10, 19, 0)
num_ddos_entries = 3821
num_normal_entries = 7895

# Generate logs
logs = generate_logs(start_time, end_time, ddos_start, ddos_end, num_ddos_entries, num_normal_entries)

# Save logs to a JSON file
with open("web_access_logs.json", "w") as f:
    json.dump(logs, f, indent=2)
