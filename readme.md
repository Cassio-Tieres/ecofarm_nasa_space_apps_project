# EcoFarm Puzzle: Agro Precision Strategy Game

### **1\. MVP Description**

#### **1.1 Problem Description**

Modern agriculture faces a dual challenge of

**sustainability and efficiency**. Although high-precision satellite environmental data (such as that provided by

**NASA**) exists, there is a critical gap in its practical application:

**How can we democratize the analysis of NASA satellite data to empower the next generation of farm managers to implement Precision Agriculture cost-effectively and sustainably, replacing the inefficiency of uniform management with intelligent and localized resource allocation?**

The project solves the problem of

**resource inefficiency** (water and fertilizers) and **low adoption of precision techniques** by transforming complex data into an accessible and strategic game mechanic.

#### **1.2 Solution Description**

**ECOFARM \- Precision Simulation** is an educational farming management simulator in a 2D isometric environment for higher education students pursuing Agronomy (bachelor's), Agricultural Engineering, Agribusiness Technology, Agribusiness Management, Agricultural Production, among other courses in the niche.

**ECOFARM uses real NASA data to teach precision agriculture, sustainability, and environmental data interpretation**. The system combines elements of simulation, strategy, and data-driven decision-making with an interactive and gamified interface, allowing students and agricultural professionals to understand, in practice, the impact of their choices on soil, productivity, and the environment.

The proposal is to integrate technical learning with entertainment, based on real satellite data such as

**NDVI** (vegetation health), **SMAP** (soil moisture), **LST** (surface temperature), and **GPM** (precipitation) collected through **NASA's open APIs**.

The player acts as the manager of a modular farm and must analyze heat maps and climate indicators to define precision management actions, such as irrigation and fertilization.

The MVP will have functionalities such as:

* **Reading of real NASA data** (NDVI, SMAP, GPM \- Giovanni, LST) integrated via API.  
* Modular isometric map, with visualization by  
   **cultivation plots**.  
* **NASA Control Panel**, displaying heat maps and soil and climate indicators.  
* Irrigation and fertilization system by  
   **management zones**.  
* **Dynamic economy**, where the player manages costs and yield.  
* Visual feedback system (healthy plants, water stress, low fertility).  
* **Scoring based on management efficiency and sustainability**.  
* Interactive tutorial mode, explaining how to interpret the in-game data.  
* **Performance reports**, showing the impact of decisions on final yield.

The solution is structured in one level of complexity:

* **Game Mode (UC01 \- Technical Simulation):** intended for students and professionals with prior knowledge, offering total control over soil and climate parameters, allowing for complex analyses and the generation of productivity and sustainability performance reports in the phase.

The MVP seeks to simulate a realistic agricultural decision-making environment, where learning occurs practically and visually, bringing the player closer to the scientific process of soil analysis and management based on spatial data.

**Key Solution Differentiators**:

* **Direct integration with NASA satellite data via API**.  
* Intuitive and accessible  
   **2D isometric interface**.  
* Data-based feedback system and performance reports.  
* **Scoring based on sustainability and management efficiency**.  
* Possibility of  
   **academic use** in courses such as Animal Science (Zootecnia), Agronomic Engineering, and Environmental Management.

ECOFARM transforms complex data into visual and interactive decisions, making the learning of precision agriculture accessible, engaging, and connected to the current technological reality of agribusiness.

---

### **1.3.0 Identified Personas for the Solution**

#### **1.3.1 Persona 1 \- João Gabriel (The Sustainable Apprentice)**

* **Age:** 19 years old  
* **Course:** Animal Science (1st semester)  
* **Objective:** To learn practically about soil management and sustainability.  
* **Context:** João has just entered the course and is looking for a tool to help him understand basic concepts like irrigation, fertilization, and environmental impact in a visual and interactive way.  
* **Motivations:**  
  * Wants to understand how NASA data influences agricultural decisions.  
  * Seeks to transform theory into practice with a simulator that facilitates learning.  
* **Challenges:**  
  * Difficulty interpreting technical soil and climate data.  
  * Lack of practical field experience.  
* **How ECOFARM helps him:**  
  * The  
     **tutorial mode** with the mascot guides João step-by-step, teaching him how to interpret maps and indicators.  
  * The visual actions and instant feedbacks facilitate learning and make studying more dynamic.

#### **1.3.2 Persona 2 \- Ana Luiza (The Agronomist Strategist)**

* **Age:** 24 years old  
* **Course:** Agronomic Engineering (8th semester)  
* **Objective:** To apply technical knowledge to optimize soil management and increase productive efficiency.  
* **Context:** Ana already masters precision agriculture concepts and is looking for a simulation that allows her to test real strategies, based on scientific data.  
* **Motivations:**  
  * Wants to compare scenarios and real management results.  
  * Seeks to develop sustainable and profitable solutions.  
* **Challenges:**  
  * Finding accessible tools that use updated and real data.  
  * Validating field hypotheses in a virtual environment.  
* **How ECOFARM helps her:**  
  * The  
     **advanced mode** allows simulating climate conditions and testing decisions based on NDVI, SMAP, and GPM.  
  * The  
     **performance reports** allow her to evaluate the economic and environmental impact of the decisions made.

#### **1.3.3 Persona 3 \- Professor Ricardo (The Innovative Educator)**

* **Age:** 38 years old  
* **Profession:** Professor in Agronomic Engineering and Animal Science  
* **Objective:** To integrate technological and interactive tools in the classroom to facilitate practical teaching.  
* **Context:** Professor at a public institution, looking for didactic resources that engage students and unite science, technology, and sustainability.  
* **Motivations:**  
  * Wants to demonstrate how real data (like NASA's) influences agricultural decisions.  
  * Seeks active teaching methodologies that stimulate students' critical thinking.  
* **Challenges:**  
  * Making technical teaching more attractive and understandable for beginners.  
  * Finding accessible platforms compatible with the academic environment.  
* **How ECOFARM helps him:**  
  * Can use the simulator as a  
     **virtual laboratory tool**.  
  * The reports and scenarios can be used as  
     **evaluation or group discussion material**.

#### **1.3.4 Persona 4 \- Camila Torres (The Sustainable Manager)**

* **Age:** 30 years old  
* **Profession:** Consultant in Precision Agriculture  
* **Objective:** To train producers and technicians in sustainable management practices using technological data.  
* **Context:** Works on consulting and environmental education projects. Seeks new tools to demonstrate concepts visually and accessibly to farmers and students.  
* **Motivations:**  
  * Wants to use ECOFARM in  
     **training and workshops**.  
  * Desires to promote awareness about the rational use of water and fertilizers.  
* **Challenges:**  
  * Explaining technical concepts to audiences with different levels of knowledge.  
  * Showing practical and measurable results clearly.  
* **How ECOFARM helps her:**  
  * Allows demonstrating the  
     **real impact of agricultural decisions in a gamified environment**.  
  * Facilitates the understanding of spatial data through heat maps and visual feedbacks.

---

### **1.4 User Journey**

#### **Beginner User Path: Guided Learning (UC01)**

This path is designed for a newly admitted student (e.g., Animal Science), whose focus is to understand the fundamentals of the game and soil management in a didactic way.

* **Access and Welcome:** The user accesses the game and is immediately greeted by a central menu, which contains three access options: **Play, Levels, and Settings**. By clicking Play, the user is directed to the match configuration screen, where they define the initial location (Locked in Sergipe for the DEMO) and one of three crop options to start, which retrieves the real-time initial condition data for the gameplay.  
* **Gameplay:** The user is greeted by a modular board, which contains their action options (**Plant, Irrigate, Fertilize, and Wait**) and a bar with the current status of their crop (**Soil Temperature, Soil Moisture, and Soil Health**). The Objective must be guided according to the selected crop, and the game will be situated in a time dimension of cycles (  
  **7 days**) which will be separated into three cultivation stages.  
* **Feedback and Consequences:** All user actions must have mapped consequences, which reflect the initial terrain conditions collected in the setup stage. After the conclusion of a stage, the user must receive feedback on their actions based on a grading system.

#### **Expert User Path (UC02) \- Simulation & Analysis**

* **Configuration and Data Analysis:** The specialist selects or creates a **custom scenario**, defining the soil type and crop. The system displays the  
   **Detailed Data Panel**. It is at this point that NASA integration becomes crucial: the player analyzes external climate data (such as Soil Temperature \- LST and Precipitation \- GPM \- Giovanni) to cross-reference with the soil indicators. The 2D interface uses graphs and icons to visualize this data, ensuring critical and informed analysis.  
* **Strategic Decision and Simulation:** The player demonstrates control by making complex and integrated decisions (e.g., defining the type and rate of fertilization, or the irrigation technique based on NASA's rain forecast). The system processes the decisions in a  
   **simulation engine** that reflects the impacts on the virtual environment.

---

### **2\. Development Planning**

#### **2.1 Customer Prioritized Product Backlog**

| ID | User Story | Description / Objective | Priority |  |
| :---- | :---- | :---- | :---- | :---- |
| **US01** | As a user, I want to view **heat maps based on NASA data** (NDVI, SMAP, LST, GPM) to make decisions about the soil. | Allow the player to see the real moisture, fertility, and vegetation of the terrain. |  | **P1** |
| **US02** | As a user, I want to be able to perform management actions (irrigate, fertilize, rotate crops) and **see the impact on the soil**. | Creates the interactive core of the simulator with immediate and educational results. |  | **P1** |
| **US03** | As a user, I want to monitor an **agricultural indicators panel** to understand the farm's productivity and sustainability. | Displays graphs and metrics such as yield, resource consumption, and environmental impact. |  | **P1** |
| **US04** | As a professional in the area, I want to access **advanced simulation scenarios** with climate variations and real data. | Expands the experience for students and technicians in Agronomic Engineering courses. |  | **P2** |
| **US05** | As a user, I want to receive **automatic reports** with results and decisions made. | Facilitates educational evaluation and learning tracking. |  | **P2** |
| **US06** | As a user, I want to view **dynamic visual feedback** (plant growth, change in soil color). | Increases engagement and understanding of the impact of actions. |  | **P2** |
| **US07** | As an advanced user, I want to **compare different areas of the farm** to plan land use. | Introduces a spatial analysis system, comparing plots and management. |  | **P3** |

#### **2.2 Core Mechanic: "Precision Mapping"**

Instead of irrigating and/or fertilizing the entire field, the player must access the

**NASA Panel** to determine which **management zones** (parts of the plot) need intervention.

* **Action:** The player clicks the top bar to access specific data for their land plot.  
* **Analysis:** On the panel, they view the NASA data heat map (NDVI, SMAP). They use selection tools to select the zone that needs treatment.  
  * **Example:** Selects the "Dry Zone" (low SMAP) and the "Low Vigor Zone B" (low NDVI).  
* **Decision:** The player decides the allocation:  
  * Zone A: Low-Intensity Irrigation.  
  * Zone B: Nitrogen Fertilizer Application.  
* **Punishment/Reward:** Financial losses (cost of the action) and visual punishments (wilted crops) only affect the zones not treated correctly.  
   **Precision treatment saves money** (fewer resources) and increases yield/soil health.

#### **2.3 Use of NASA Data (Agriculture and Water Management Pathfinder)**

The game must force the player to interpret the connections between the data:

| Data Set (Pathfinder) | In-Game Visualization | Player Decision |  |  |
| :---- | :---- | :---- | :---- | :---- |
|  | **Soil Moisture (SMAP)** | Heat map " | **Water Level**" | Determines the volume and intensity of irrigation per zone. |
|  | **Vegetation Health (NDVI)** | Heat map " | **Plant Vigor**" | Determines the need and type of fertilizer (precision nutrition). |
|  | **Surface Temperature (LST)** | Heat map " | **Thermal Stress**" | Used to plan planting/harvest time and simulate heat stress or frost events. |
|  | **Precipitation (GPM)** | Line graph/table " | **Climate History**" | Used to project drought or flood risk and schedule the irrigation cycle. |

#### **2.4 Educational and Economic Elements**

* **Soil Health (Sustainability):** Maintain a "**Soil Health**" bar.  
   **Excessive resource use** (excess fertilizer, unnecessary irrigation) leads to invisible costs (pollution, degradation) that decrease land value and future yield.  
* **Soil Moisture (Sustainability):** Keep the soil hydrated. The use of the game's irrigation resources alters the initial rates mapped based on GPM.

This

**Precision Simulation** concept is highly aligned with the challenge, focusing gameplay directly on the interpretation of NASA data for precision agriculture decision-making, and is totally feasible in a 2D/isometric environment.

---

### **2.5 Optimization and Reports**

After the simulation, the system generates a

**Performance Report** that details the consequences of the player's actions in key metrics: **Productivity, Crop Success, and Sustainability/Environmental Impact**. It offers a technical comment on the result or suggests alternatives if there is a serious error (e.g., excessive use of inputs). This phase allows the player to compare strategies and

**optimize their management plan**, generating reports that can be used for study or experimentation.

### **3\. Technical Specification**

#### **3.1 Development Stacks**

* **Prototyping:** Figma  
* **Implementation:**  
  * Backend:  
     **Node.js** (for data management, requests, and integration with external APIs), **Nest js, View js, Docker**.  
  * Database:  
     **MYSQL** (real-time cloud storage) and **MongoDB**.  
* **Integrations:**  
  * **NASA APIs (Earthdata / Open Data):** use of NDVI, SMAP, and GPM.  
  * **OpenWeatherMap:** to simulate real-time climate conditions (temperature, rain, humidity).  
  * OAuth 2.0 (Google): login and secure user authentication (post-MVP phase).  
* **Versioning:** Git and Github.

#### **3.2 System Structure**

* **Interface Module (UI):** displays the isometric farm map and the NASA control panel.  
* **Data Module:** receives and processes external information (NDVI, SMAP, LST, GPM) in real-time.  
* **Game Logic Module:** manages player actions (irrigate, fertilize, analyze terrain).  
* **Visual Feedback Module:** updates soil and crop conditions based on decisions.  
* **Final Feedback Module:** User performance report after the conclusion of a phase.  
* **Storage Module:** saves progress, settings, and performance reports.

#### **3.3 USE CASE**

**Use Case: Interactive Tutorial Guided by the Mascot**

* **Identifier:** UC01  
* **Name:** Learn to play and understand soil care  
* **Main Actor:** Beginner player (Animal Science student)  
* **Brief Description:** A student newly admitted to the Animal Science course accesses the application to learn about soils and agricultural care. They access the setup menu through a Play button, which allows choosing an initial harvest, their geolocation, and receives their initial parameters.  
* **Main Flow:**  
  * The user starts the application for the first time.  
  * The mascot guides the player to perform their first action (e.g., fertilize or irrigate).  
  * The system shows the results of this action in real-time.  
  * The mascot explains the consequences of not performing adequate care (such as soil infertility or production drop).  
  * The player concludes the tutorial and is directed to the main game mode.  
* **Alternative Flows:**  
  * **A1:** The player skips the tutorial.  
  * The system asks if they really want to skip.  
  * If confirmed, the game starts in free mode, but the mascot remains available for quick tips.  
* **Pre-conditions:** The player must have installed the application and created a profile.  
* **Post-conditions:** The player understands the basic concepts of using the application and how to care for the soil within the game.

**UC-MVP-01 — Start Simulation (Setup Stage)**

* **Objective:** Allow the player to select a location (geolocation) and an agricultural crop to load environmental data (SMAP and GPM) and start the first level of the simulation.  
* **Actors:** Player.  
* **Pre-conditions:**  
  1. The game has been started on the initial screen ("Play").  
  2. The player has internet access to load NASA data.  
* **Main Flow:**  
  1. The player accesses the  
      **Setup Stage** screen.  
  2. Selects a location (e.g., Sergipe) and a crop (e.g., corn).  
  3. The system consults:  
     * **SMAP** (Soil Moisture Active Passive) → superficial soil moisture value.  
     * **GPM/IMERG V07** → accumulated value of recent precipitation (24h/7 days).  
  4. The system loads the  
      **Level 1 Objective**: "The plants are slightly wilted and the soil looks dry. Find out what is missing".  
  5. The player presses  
      **Start** to begin the level.  
* **Post-conditions:** The environment is configured with the initial bars for Precipitation, Moisture, and Soil Health.

**UC-MVP-02 — Make Management Decisions (Actions 0/3)**

* **Objective:** Allow the player to interpret climate indicators and make soil management decisions (irrigate, fertilize, or wait) during three turns.  
* **Actors:** Player.  
* **Pre-conditions:**  
  * Level started (via UC-MVP-01).  
  * Indicators displayed at the top of the screen:  
    * Precipitation (rain \- GPM)  
    * Moisture (humidity \- SMAP)  
    * Soil Health (internal index)  
* **Main Flow (Example of Correct Path):**  
  * **Turn 1 – Player chooses Fertilize**.  
    * Feedback: "The problem may not be nutritional".  
    * Moisture remains low (  
      ∼25%).  
  * **Turn 2 – Player chooses Irrigate**.  
    * Feedback: "Excellent\! Irrigation is helping the plants recover".  
    * Moisture increases to  
       ∼65%.  
  * **Turn 3 – Player chooses Wait**.  
    * Feedback: "Good\! Allowing recovery time was crucial".  
    * Soil Health rises to  
       ∼80%.  
  * The system displays  
     **Stage Complete**.  
* **Alternative Flow (Incorrect Path):**  
  * Turn 1 – Fertilize, no effect (Critical Moisture).  
  * Turn 2 – Wait, negative feedback: "The problem may not be this".  
  * Turn 3 – No irrigation  
     → Moisture 15%, Soil Health 15%.  
  * Final Result:  
     **Grade F** ("Need to work on it").  
* **Business Rules:**  
  * **Irrigate** is only effective with Moisture \<40%.  
  * **Wait** is recommended if Precipitation \>80%.  
  * **Fertilize** without sufficient moisture reduces Soil Health.  
* **Post-conditions:** System calculates averages and determines final grade (A–F).

**UC-MVP-03 — Display Stage Result (Station Result)**

* **Objective:** Show the player the final score and allow them to proceed linearly to the next level.  
* **Actors:** Player.  
* **Pre-conditions:** Level completed (UC-MVP-02).  
* **Main Flow:**  
  * The system displays  
     **Station Result**.  
  * Shows:  
    * Final Grade (A–F).  
    * Seal ("Conscious Farmer," "Need to work on it").  
    * Final Averages for Precipitation, Moisture, and Soil Health.  
  * Player presses  
     **Continue**.  
  * The next level starts automatically.  
* **Post-conditions:** Linear progress: Level 1→2→3. After Level 3, the game returns to the main menu.  
* **Evaluation Rules:** (Based on the Help \> How to Progress screen)  
  * **A:** average ≥70%.  
  * **B:** average between 50%–70%.  
  * **C:** average between 30%–50%.  
  * **D/F:** average \<30%.

**UC-MVP-04 — Consult Help (Help Menu)**

* **Objective:** Help the player understand the indicators and the game logic based on NASA data.  
* **Actors:** Player.  
* **Pre-conditions:** The player accesses ? (Help)  
   during any screen.  
* **Main Flow:**  
  1. System displays  
      **Help Menu**.  
  2. Player chooses one of the options:  
     * "What is the Objective"  
     * "How to Play"  
     * "How to Progress Levels"  
  3. The system shows:  
     * Explanation of indicators:  
       * **Precipitation:** "Indicates the volume of rain, directly affects moisture".  
       * **Moisture:** "Essential for growth; keep above 40%".  
       * **Soil Health:** "General soil quality; above 70% is excellent".  
     * Management tips: "Observe the climate before acting. Balance irrigation and fertilization".  
     * Progress criteria (A/B advance to the next level).  
* **Post-conditions:** Player understands how the indicators work and returns to the game.

**UC-MVP-05 — Configure Preferences (Configuration)**

* **Objective:** Allow the player to adjust language and audio volume.  
* **Actors:** Player.  
* **Pre-conditions:** Game started; access to the **"Configuration"** screen.  
* **Main Flow:**  
  1. Player adjusts  
      **Language** (EN/PT-BR).  
  2. Adjusts  
      **Volume** (slider 20%–80%).  
  3. Clicks  
      **Save**.  
  4. Preferences are applied immediately.

#### **3.4 Data Collection**

1. **Data sources:**  
   * **SMAP** (Soil Moisture Active Passive): For collecting data related to soil health \- SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture V006 | Earthdata Search.  
   * **Giovanni** (Geospatial Interactive Online Visualization ANd aNalysis Infrastructure) with **GPM** (Global Precipitation Measurement): For collecting climatological precipitation data \- Giovanni.  
   * **LST & NDVI** (DEMO)

## **References:**

https://www.figma.com/design/lRZRhq6A6ElbnEOa3iAZ2m/Pixel-Game-User-Interface--Community-?node-id=103-4573\&t=ujnjY1MIIwqdp8oG-1

NASA. *Data access tools for agriculture production (Human Dimensions).* Disponível em: [https://www.earthdata.nasa.gov/topics/human-dimensions/agriculture-production/data-access-tools?page=%2C0](https://www.earthdata.nasa.gov/topics/human-dimensions/agriculture-production/data-access-tools?page=%2C0). Acesso em: 4 out. 2025\.

NASA. *NASA Farm Navigators: Using NASA Data Exploration in Agriculture — Details.* In: *NASA Space Apps Challenge 2025\.* Disponível em: [https://www.spaceappschallenge.org/2025/challenges/nasa-farm-navigators-using-nasa-data-exploration-in-agriculture/?tab=details](https://www.spaceappschallenge.org/2025/challenges/nasa-farm-navigators-using-nasa-data-exploration-in-agriculture/?tab=details). Acesso em: 4 out. 2025\.

NASA. *NASA Farm Navigators: Using NASA Data Exploration in Agriculture — Resources.* In: *NASA Space Apps Challenge 2025\.* Disponível em: [https://www.spaceappschallenge.org/2025/challenges/nasa-farm-navigators-using-nasa-data-exploration-in-agriculture/?tab=resources](https://www.spaceappschallenge.org/2025/challenges/nasa-farm-navigators-using-nasa-data-exploration-in-agriculture/?tab=resources). Acesso em: 4 out. 2025\.

**References UI**

PIXEL Game User Interface. Figma Community. \[S. l.\]: Figma, \[entre 2023 e 2025\]. Disponível em:[Pixel Game User Interface (Community) – Figma](https://www.figma.com/design/lRZRhq6A6ElbnEOa3iAZ2m/Pixel-Game-User-Interface--Community-?node-id=103-4573&t=ujnjY1MIIwqdp8oG-1). Acesso em: 5 out. 2025\.

JAMES, Ryder. Pixel UI Pack. \[S. l.\]: Itch.io, \[2023\]. Disponível em: [https://ryder-james.itch.io/pixel-ui-pack](https://ryder-james.itch.io/pixel-ui-pack). Acesso em: 5 out. 2025\.

HACKERNOON. Pixel Icon Library: Open-Source Pixelated Icons By HackerNoon. \[S. l.\]: HackerNoon, \[2024\]. Disponível em: [https://pixeliconlibrary.com/](https://pixeliconlibrary.com/). Acesso em: 5 out. 2025\.

BDRAGON1727. Pixel UI Button Icon Platformer Free. \[S. l.\]: Itch.io, \[2022\]. Disponível em: [https://bdragon1727.itch.io/pixel-ui-button-icon-platformer](https://bdragon1727.itch.io/pixel-ui-button-icon-platformer). Acesso em: 5 out. 2025\.

PIXELLAB. AI Pixel Art Generator for Game Development. \[S. l.\]: PixelLab, \[2025\]. Disponível em: [https://www.pixellab.ai/](https://www.pixellab.ai/). Acesso em: 5 out. 2025\.

