import json
from linkedin_api import Linkedin

# Authenticate LinkedIn API
api = Linkedin('kumhgjgjjhjjhvh@gmail.com', 'jhhfgxzh')

# Get profile input
profile = input("Enter your LinkedIn profile ID or URL: ").strip()

# Clean URL if full link is pasted
if "linkedin.com/in/" in profile:
    profile = profile.split("linkedin.com/in/")[1].strip("/")

try:
    profile_data = api.get_profile(profile)

    # Extract formatted profile
    formatted_profile = {
        "name": profile_data.get("firstName", "") + " " + profile_data.get("lastName", ""),
        "current_designation": profile_data.get("headline", ""),
        "current_company": profile_data.get("experience", [{}])[0].get("companyName", ""),
        "current_tenure": profile_data.get("experience", [{}])[0].get("timePeriod", ""),
        "overall_experience": "",  # Optional to calculate
        "location": profile_data.get("locationName", ""),
        "education": [
            {
                "institution": edu.get("schoolName", ""),
                "degree": edu.get("degreeName", ""),
                "duration": f"{edu.get('timePeriod', {}).get('startYear', '')} – {edu.get('timePeriod', {}).get('endYear', '')}"
            }
            for edu in profile_data.get("education", [])
        ],
        "skills": profile_data.get("skills", []),
        "connections_count": profile_data.get("connections", "500+"),
        "is_open_to_work": profile_data.get("openToWork", False)
    }

    # Print to terminal
    print(json.dumps(formatted_profile, indent=4))

    # Save to a JSON file
    with open("linkedin_profile.json", "w") as f:
        json.dump(formatted_profile, f, indent=4)

    print("Profile saved to linkedin_profile.json")

except Exception as e:
    print("Failed to fetch profile. Error:", str(e))

