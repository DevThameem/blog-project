from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random




class Command(BaseCommand):
    help = "This command insert post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing Data
        Post.objects.all().delete()

        titles = [
            "How to Build a Personal Brand from Scratch",
            "The Benefits of Minimalist Living",
            "The Rise of Remote Work: What You Need to Know",
            "10 Essential Tips for Effective Time Management",
            "The Psychology Behind Color Choices in Marketing",
            "How to Start a Successful Freelance Career",
            "A Beginner's Guide to Meditation and Mindfulness",
            "The Future of Artificial Intelligence in Everyday Life",
            "How to Create a Sustainable Fashion Wardrobe",
            "The Importance of Digital Detox: Unplugging for Mental Health",
            "Exploring the Best Hiking Trails Around the World",
            "How to Grow Your Own Organic Vegetable Garden",
            "The Impact of Social Media on Mental Health",
            "10 Ways to Boost Your Creativity Every Day",
            "How to Manage Personal Finances Like a Pro",
            "Why You Should Start Journaling for Better Self-Reflection",
            "The Art of Negotiation: Tips for Getting What You Want",
            "The Benefits of Practicing Gratitude Daily",
            "How to Improve Your Public Speaking Skills",
            "A Complete Guide to Hosting the Perfect Dinner Party",
            "Why Reading Books Can Change Your Life",
            "How to Stay Productive During the Winter Months",
            "The Power of Networking: Building Meaningful Connections",
            "How to Master the Art of Self-Care",
            "Exploring the World of Plant-Based Eating"
        ] 

        contents = [
            "Start by defining your values, identifying your niche, and establishing a strong online presence. Consistency and authenticity are key to building a lasting personal brand.",
            "Minimalism reduces clutter and stress, enhances focus, and promotes sustainability. By embracing simplicity, you can live a more intentional, fulfilling life with less.",
            "Remote work offers flexibility and convenience. However, it comes with challenges like isolation and distractions. Setting boundaries and staying organized are crucial for success.",
            "Prioritize tasks, set SMART goals, avoid multitasking, and take breaks. Using tools like calendars or time-blocking can help increase productivity and reduce stress.",
            "Colors influence emotions and perceptions. For example, red evokes urgency, blue fosters trust, and yellow stimulates happiness. Understanding color psychology enhances marketing effectiveness.",
            "Build a portfolio, set clear rates, and network effectively. Freelancing requires discipline, strong communication, and marketing skills. Establishing a personal brand helps attract clients.",
            "Meditation enhances mindfulness, reduces stress, and promotes emotional well-being. Start with short sessions, focus on your breath, and gradually extend practice for maximum benefits.",
            "AI is transforming industries, from healthcare to transportation. Expect smarter homes, personalized services, and advancements in automation, changing how we live and work.",    "Taking breaks from screens restores mental clarity and reduces stress. A digital detox helps you reconnect with the present, improve sleep, and nurture relationships.",
            "Build a wardrobe with eco-friendly, durable, and versatile pieces. Focus on quality, shop secondhand, and opt for ethical brands to reduce fashion's environmental impact.",
            "Taking breaks from screens restores mental clarity and reduces stress. A digital detox helps you reconnect with the present, improve sleep, and nurture relationships.",
            "Discover breathtaking hiking trails worldwide, from the Swiss Alps to the Appalachian Mountains. Enjoy nature’s beauty, challenge yourself, and enhance physical and mental well-being.",
            "Start with nutrient-rich soil, select organic seeds, and maintain consistent watering. Growing your own veggies reduces costs, promotes healthy eating, and supports sustainability.",
            "Social media can increase anxiety and depression, fostering comparison and unrealistic standards. Balance online presence with self-care and limit exposure to negative content.",
            "Stay inspired by practicing brainstorming, journaling, and embracing new experiences. Change routines, explore different hobbies, and surround yourself with creative people and environments.",
            "Budgeting, saving, investing, and minimizing debt are key to financial success. Set clear financial goals, track spending, and prioritize long-term stability over short-term indulgences.",
            "Journaling enhances self-awareness and emotional clarity. Write daily to process thoughts, set goals, and track personal growth. It promotes mindfulness and stress reduction.",
            "Successful negotiation requires preparation, active listening, and compromise. Be clear on your needs, remain calm, and aim for mutually beneficial solutions to achieve success.",
            "Daily gratitude boosts happiness and well-being by shifting focus to the positive. It enhances relationships, reduces stress, and cultivates an optimistic outlook on life.",
            "Overcome nerves by practicing regularly, maintaining eye contact, and focusing on your message. Mastering body language and engaging your audience boosts your speaking confidence.",
            "Plan your menu, set a welcoming atmosphere, and communicate with guests. Balance food, drink, and entertainment while ensuring everyone feels comfortable and included.",
            "Reading expands knowledge, improves focus, and enhances empathy. Books stimulate the imagination, offer new perspectives, and inspire personal and professional growth.",
            "Combat winter lethargy by maintaining a routine, setting clear goals, and staying active. Use natural light, focus on cozy workspaces, and practice self-care for motivation.",
            "Networking fosters professional growth and personal relationships. Attend events, engage online, and nurture connections by offering value, staying in touch, and showing genuine interest.",
            "Self-care enhances mental, physical, and emotional health. Practice relaxation techniques, prioritize sleep, nourish your body, and set aside time for hobbies and reflection.",
            "Plant-based eating boosts health, supports sustainability, and reduces environmental impact. Start by incorporating more vegetables, fruits, grains, and legumes into meals for better nutrition."
        ]

        img_url = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
            "https://picsum.photos/id/21/800/400",
            "https://picsum.photos/id/22/800/400",
            "https://picsum.photos/id/23/800/400",
            "https://picsum.photos/id/24/800/400",
            "https://picsum.photos/id/25/800/400"

        ]
        
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_url):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)  

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))     
        


