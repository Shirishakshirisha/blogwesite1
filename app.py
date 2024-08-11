from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

# Sample blog data
blogs = [
    {"id": 1, "title": "The Disaster Recovery Blog", "url": "https://www.disasterrecoveryjournal.com/", "description": "Articles and insights on disaster recovery planning, business continuity, and emergency preparedness."},
    {"id": 2, "title": "The Emergency Management Blog", "url": "https://www.emergencymanagement.com/", "description": "News and articles on emergency management practices, disaster preparedness, and response strategies."},
    {"id": 3, "title": "Ready.gov Blog", "url": "https://www.ready.gov/blog", "description": "Tips on preparing for emergencies, including emergency kits and planning for specific disasters."},
    {"id": 4, "title": "American Red Cross Blog", "url": "https://www.redcross.org/about-us/news-and-media.html", "description": "Posts about disaster preparedness, personal safety tips, and the Red Cross’s response to emergencies."},
    {"id": 5, "title": "Preparedness Blog by The Survivalist Blog", "url": "https://www.thesurvivalistblog.net/", "description": "Topics related to survival, preparedness, and self-sufficiency."},
    {"id": 6, "title": "The Modern Survival Blog", "url": "https://modernsurvivalblog.com/", "description": "Practical tips for disaster preparedness, survival strategies, and emergency planning."},
    {"id": 7, "title": "Be Prepared Blog", "url": "https://www.beprepared.com/blog/", "description": "Advice on emergency preparedness, product reviews, and survival tips."},
    {"id": 8, "title": "National Geographic's Disaster Blog", "url": "https://www.nationalgeographic.com/environment", "description": "Articles on natural disasters, environmental risks, and their impact on communities."},
    {"id": 9, "title": "Emergency Management Today", "url": "https://www.emergencymanagementtoday.com/", "description": "Covers current trends, best practices, and news in the field of emergency management and disaster response."},
    {"id": 10, "title": "The Prepared Blog", "url": "https://theprepared.com/", "description": "Provides in-depth guides and articles on emergency preparedness, survival skills, and practical advice for handling various types of disasters."},
    {"id": 11, "title": "Survival Blog", "url": "https://survivalblog.com/", "description": "Offers a wide range of articles on survival tactics, preparedness strategies, and reviews of emergency supplies."},
    {"id": 12, "title": "CDC Disaster Preparedness Blog", "url": "https://www.cdc.gov/nceh/infection_control/index.html", "description": "Provides information on preparing for natural and man-made disasters, including health and safety tips."},
    {"id": 13, "title": "The Survival Podcast", "url": "https://www.thesurvivalpodcast.com/", "description": "Features podcasts and blog posts on survival strategies, self-reliance, and disaster preparedness."},
    {"id": 14, "title": "Be Ready Blog by the State of Utah", "url": "https://bereadyutah.gov/", "description": "Offers resources and tips for preparing for emergencies, including community preparedness and personal safety."},
    {"id": 15, "title": "WHO Emergency Preparedness Blog", "url": "https://www.who.int/emergencies", "description": "Covers global emergency preparedness and response strategies, including health-related emergencies."},
    {"id": 16, "title": "Prepper Journal", "url": "https://www.theprepperjournal.com/", "description": "Features articles on emergency preparedness, survival strategies, and prepping for various scenarios."},
    {"id": 17, "title": "The Emergency Prep Guy", "url": "https://www.emergencyprepblog.com/", "description": "Provides tips, guides, and articles on emergency preparedness and survival planning."},
    {"id": 18, "title": "My Family Survival Plan", "url": "https://myfamilysurvivalplan.com/", "description": "Offers advice on survival skills, emergency preparedness, and family safety during disasters."}
]

@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)

@app.route('/')
def serve_home():
    return send_from_directory('', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(debug=True)
