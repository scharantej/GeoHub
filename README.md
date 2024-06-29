## Flask Application Design

### HTML Files

- **index.html**:
  - Home page. Features a banner section with a looping MP4 video, static image assets, company description, and call to action for a free consultation.
- **solutions.html**:
  - Solutions page. Displays detailed information on geothermal energy solutions for different industries. Includes case studies, testimonials, and a call to action to request a quote.
- **news.html**:
  - News page. Presents recent news and articles about the company and the geothermal energy industry. Includes social media sharing buttons.
- **about-us.html**:
  - About Us page. Provides the company's history, mission, values, and team section with member photos and bios.
- **contact-us.html**:
  - Contact Us page. Offers multiple contact options, including a form, phone number, email address, physical address, and an interactive map.

### Routes

- **@app.route('/')**:
  - Main route, displays the **index.html** home page.
- **@app.route('/solutions')**:
  - Solution page route, renders the **solutions.html**.
- **@app.route('/news')**:
  - News page route, displays the **news.html**.
- **@app.route('/about-us')**:
  - About Us page route, renders the **about-us.html**.
- **@app.route('/contact-us')**:
  - Contact Us page route, displays the **contact-us.html**.