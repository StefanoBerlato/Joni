# Joni 
When a person becomes blind he loses all his points of reference. Everyday life and actions become extremely difficult and, even though basic tasks are learned through experience and practice, there are still some issues when it comes to the interaction with technology. Unfortunately, there are few, complicated and expensive devices for blind people, and often they are detached from their old world.

Our solution, Joni, will help blind and visually impaired people to keep in touch with the world, paying attention to both costs and user experience. We propose a handheld internet-connected physical device that allows users to listen to the latest and tailored news, whenever and wherever they want it. With few and simple buttons and an easy menu navigation, the users will be able to select their preferred news categories, listen to the related news and manage settings (e.g volume of speakers)

In particular, our prototype is made of these components: 
* A Raspberry for information and input processing with buttons and wires.
* A 3G USB Dongle with a SIM card for internet connectivity.
* A frontal speaker to reproduce audio.
* A power bank battery to power the other components.

Of course, there is also a web server that, asynchronously, fetches the news through an external service (NewsAPI https://newsapi.org/) and converts them using Google Text-To-Speech service (https://github.com/zlargon/google-tts).

This is part of a university project called "Joni" developed by a team of Trento University's students for the Business Development Lab and ICT Innovation courses.  
