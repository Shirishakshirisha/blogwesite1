document.addEventListener('DOMContentLoaded', function() {
    const blogs = [
        {
            id: 1,
            title: "Understanding Emergency Preparedness",
            url: "https://www.ready.gov/prepare",
            description: "Comprehensive guide on how to prepare for emergencies and natural disasters."
        },
        {
            id: 2,
            title: "Top 10 Emergency Kits for Families",
            url: "https://www.cdc.gov/disasters/preparekit.html",
            description: "Essential items for building a family emergency kit to handle various disasters."
        },
        {
            id: 3,
            title: "How to Create a Disaster Plan",
            url: "https://www.fema.gov/emergency-managers/risk-management/plan",
            description: "Step-by-step instructions on creating a robust disaster plan for your family."
        },
        {
            id: 4,
            title: "The Role of Community in Disaster Response",
            url: "https://www.redcross.org/get-help/how-to-prepare-for-emergencies.html",
            description: "Explains how community involvement can enhance disaster response efforts."
        },
        {
            id: 5,
            title: "Emergency Response Team Operations",
            url: "https://www.fema.gov/emergency-managers/incident-management",
            description: "Insights into how emergency response teams operate and their roles during disasters."
        },
        {
            id: 6,
            title: "First Aid Basics for Disasters",
            url: "https://www.redcross.org/take-a-class/first-aid",
            description: "Fundamentals of first aid and its importance in emergency situations."
        },
        {
            id: 7,
            title: "Understanding Natural Disasters",
            url: "https://www.ncdc.noaa.gov/sotc/national/202106",
            description: "Detailed information on different types of natural disasters and their impacts."
        },
        {
            id: 8,
            title: "Building Resilience Against Disasters",
            url: "https://www.nibib.nih.gov/news-events/newsroom/resilient-communities",
            description: "Strategies for building personal and community resilience to withstand disasters."
        },
        {
            id: 9,
            title: "Flood Preparedness and Safety Tips",
            url: "https://www.floodsmart.gov/",
            description: "Tips and strategies for preparing for and staying safe during floods."
        },
        {
            id: 10,
            title: "How to Prepare for Hurricanes",
            url: "https://www.weather.gov/safety/hurricane",
            description: "Guidance on preparing for hurricanes, including evacuation and safety measures."
        },
        {
            id: 11,
            title: "Wildfire Preparedness and Response",
            url: "https://www.nifc.gov/fireInfo/fireInfo_main.html",
            description: "Information on preparing for and responding to wildfires."
        },
        {
            id: 12,
            title: "Earthquake Safety Tips",
            url: "https://earthquake.usgs.gov/learn/kids",
            description: "Safety tips and educational resources for understanding and preparing for earthquakes."
        }
    ];

    const blogsList = document.getElementById('blogs-list');
    blogsList.innerHTML = blogs.map(blog => `
        <li>
            <a href="${blog.url}" target="_blank">${blog.title}</a>
            <p>${blog.description}</p>
        </li>
    `).join('');
});
