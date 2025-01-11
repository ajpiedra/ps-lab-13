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
    ("198.51.100.88", "-58.3838", "-34.6146"),# Buenos Aires, Argentina (alt IP)
    ("192.168.1.99", "77.1025", "28.7041"),   # New Delhi, India
    ("198.51.100.123", "74.0060", "40.7128"),# New York, USA (alt IP)
    ("192.0.2.142", "139.6503", "35.6762"),  # Tokyo, Japan (alt IP)
    ("198.51.100.156", "2.2945", "48.8584"), # Paris, France (alt IP)
    ("203.0.113.168", "31.2357", "30.0444"),  # Cairo, Egypt (alt IP)
    ("203.0.113.10", "2.3522", "48.8566"),  # France
    ("198.51.100.20", "13.4050", "52.5200"),  # Germany
    ("192.0.2.33", "-73.935242", "40.730610"),  # New York City, USA
    ("203.0.113.34", "28.9784", "41.0082"),     # Istanbul, Turkey
    ("198.51.100.89", "12.4964", "41.9028"),    # Rome, Italy
    ("192.0.2.55", "144.9631", "-37.8136"),     # Melbourne, Australia (alt IP)
    ("203.0.113.45", "-122.6765", "45.5235"),   # Portland, USA
    ("198.51.100.67", "37.7749", "-122.4194"),  # San Francisco, USA (alt IP)
    ("192.0.2.78", "2.1734", "41.3851"),        # Barcelona, Spain
    ("203.0.113.89", "13.4105", "52.5200"),     # Berlin, Germany
    ("198.51.100.101", "139.6917", "35.6895"),  # Tokyo, Japan (another alt IP)
    ("192.0.2.90", "151.2093", "-33.8688"),     # Sydney, Australia (yet another alt)
    ("203.0.113.99", "19.0825", "72.7411"),  # Mumbai, India
    ("198.51.100.111", "-33.9186", "18.4233"),  # Cape Town, South Africa
    ("192.0.2.121", "6.5244", "3.3792"),    # Lagos, Nigeria
    ("203.0.113.132", "-43.2094", "-22.9119"),  # Rio de Janeiro, Brazil
    ("198.51.100.143", "151.2148", "-33.8688"),  # Sydney, Australia (yet another alt)
    ("192.0.2.154", "103.851959", "1.290270"),  # Singapore (alt IP)
    ("203.0.113.165", "37.9838", "23.7275"),  # Athens, Greece
    ("198.51.100.176", "139.731992", "35.709026"),  # Tokyo, Japan (another alt IP)
    ("192.0.2.187", "34.052235", "-118.243683"),  # Los Angeles, USA (alt IP)
    ("203.0.113.198", "40.712776", "-74.005974"),  # New York, USA (yet another alt)
    ("192.0.2.200", "-77.0369", "38.9072"),  # Washington, D.C., USA
    ("203.0.113.211", "-0.118092", "51.509865"),  # London, UK (alt IP)
    ("198.51.100.222", "72.8777", "19.0760"),  # Mumbai, India (alt IP)
    ("192.0.2.233", "12.5683", "55.6761"),  # Copenhagen, Denmark
    ("203.0.113.244", "174.7655", "-36.8509"),  # Auckland, New Zealand
    ("198.51.100.255", "77.5946", "12.9716"),  # Bangalore, India
    ("192.0.2.112", "35.689487", "139.691706"),  # Tokyo, Japan (one more alt)
    ("203.0.113.123", "4.3517", "50.8503"),  # Brussels, Belgium
    ("198.51.100.134", "2.3522", "48.8566"),  # Paris, France (yet another alt)
    ("192.0.2.145", "31.2357", "30.0444"),  # Cairo, Egypt (yet another alt)
    ("203.0.113.156", "106.8650", "-6.1751"),  # Jakarta, Indonesia
    ("198.51.100.167", "-43.1729", "-22.9028"),  # Rio de Janeiro, Brazil (alt)
    ("192.0.2.178", "30.5234", "50.4501"),  # Kiev, Ukraine
    ("203.0.113.189", "23.729359", "37.983810"),  # Athens, Greece (alt)
    ("198.51.100.200", "10.75", "59.91"),  # Oslo, Norway
    ("192.0.2.211", "-46.6333", "-23.5505"),  # São Paulo, Brazil
    ("203.0.113.222", "50.1109", "8.6821"),  # Frankfurt, Germany
    ("198.51.100.233", "2.159", "41.376"),  # Barcelona, Spain (alt)
    ("192.0.2.244", "-98.4936", "29.4241"),  # San Antonio, USA
    ("203.0.113.255", "118.795", "32.060"),  # Nanjing, China
    ("198.51.100.266", "-73.855", "41.295"),  # White Plains, USA
    ("192.0.2.277", "112.98", "28.23"),  # Changsha, China
    ("203.0.113.288", "21.0122", "52.2297"),  # Warsaw, Poland
    ("198.51.100.299", "-115.173", "36.114"),  # Las Vegas, USA
    ("192.0.2.310", "-0.963", "37.389"),  # Sevilla, Spain
    ("203.0.113.321", "1.511", "52.631"),  # Norwich, UK
    ("198.51.100.332", "18.692", "63.825"),  # Östersund, Sweden
    ("192.0.2.343", "7.420", "-0.228"),  # Ghana, Accra
    ("203.0.113.354", "100.516", "13.756"),  # Bangkok, Thailand
    ("198.51.100.365", "-58.381", "-34.603"),  # Buenos Aires, Argentina (alt alt)
    ("192.0.2.376", "90.393", "23.79"),  # Dhaka, Bangladesh
    ("203.0.113.387", "50.45", "26.23"),  # Zhytomyr, Ukraine
    ("198.51.100.398", "-23.54", "64.135"),  # Reykjavik, Iceland
    ("192.0.2.409", "113.57", "22.21"),  # Zhongshan, China
    ("203.0.113.420", "79.87", "6.927"),  # Colombo, Srilanka
    ("198.51.100.431", "35.3", "32.1"),  # Beirut, Lebanon
    ("192.0.2.442", "101.686", "3.139"),  # Kuala Lumpur, Malaysia
    ("203.0.113.453", "31.235711", "30.044387"),  # Cairo, Egypt (one more alt)
    ("198.51.100.464", "2.35222", "48.85661"),  # Paris, France (another alt)
    ("192.0.2.475", "139.69171", "35.68951"),  # Tokyo, Japan (one more alt)
    ("203.0.113.486", "72.8777", "19.0760"),  # Mumbai, India (alt alt)
    ("198.51.100.497", "10.7", "59.91"),  # Oslo, Norway (alt)
    ("192.0.2.508", "2.163", "48.844"),  # Marseille, France
    ("203.0.113.519", "127.463", "36.33"),  # Daejeon, South Korea
    ("198.51.100.530", "18.96", "27.18"),  # Grängesberg, Sweden
]

# Predefined mappings of IPs to locations for DDoS attacks
ddos_ips_locations = [
    ("192.0.2.30", "-0.1278", "51.5074"),    # UK
    ("203.0.113.77", "-43.1729", "-22.9068"),# Rio de Janeiro, Brazil
    ("203.0.113.111", "3.1589", "19.0758"),  # Mumbai, India
]

# Function to generate a log entry
def generate_log_entry(timestamp, ip, user_agent, location, method, url, status_code, referrer, response_time_ms):
    return {
        "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ip": ip,
        "user_agent": user_agent,
        "location": f"POINT ({location[1]} {location[0]})",
        "method": method,
        "url": url,
        "status_code": status_code,
        "referrer": referrer,
        "response_time_ms": response_time_ms[0]
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
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.pluralsight.com",
        "https://www.linkedin.com",
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
num_normal_entries = 27895

# Generate logs
logs = generate_logs(start_time, end_time, ddos_start, ddos_end, num_ddos_entries, num_normal_entries)

# Save logs to a JSON file
with open("web_access_logs.json", "w") as f:
    for line in logs:
        f.write(f"{json.dumps(line)}\n")
