# UMD Undergraduate Admissions — Programs Page

> Source: <https://admissions.umd.edu/programs> — extracted 2026-07-28.
> Program data comes from a Craft CMS **GraphQL** endpoint: `POST https://admissions.umd.edu/graphql`
> (Bearer token in `programs.js`; query name `ProgramsList`, entry type `programs_default_Entry`).
> Full raw JSON response saved verbatim to `briefs/programs-data.json`.

## Overview

- **Hero copy:** "With over 100 undergraduate majors across 12 colleges and schools, we have you covered."
- The page renders **no static program list** in HTML — it is a client-side filtered explorer. `programs.js` posts a GraphQL query and renders results into an alphabetical, faceted grid. Each program card shows the program **name** (linked to the department page), its **type label(s)**, and a description.
- **Total programs returned: 203** (unfiltered `orderBy: "title"`).
- Programs are grouped alphabetically A–Z (with an alphabet quick-nav). Each program may carry multiple type labels (e.g. both Major and Minor, or Major + Limited Enrollment Program).

## Filter facets

The UI exposes a keyword **search box** plus four multi-select facet groups (GraphQL variables in parentheses), a **Reset filters** control, and a **Done** button. Results also default to A–Z alphabetical order (`orderBy: "title"`).

### 1. Search (`searchQuery`)
Free-text keyword box that filters program titles/descriptions.

### 2. Explore by Program Types (`programCategories` → `categoryProgramTypeMultiple`)
- Major (104)
- Minor (104)
- Limited Enrollment Program (26)
- Certificate (8)
- Pre-Professional Program (13)

### 3. Explore by Colleges & Schools (`collegeCategories` → `categoryProgramCollegesSchoolsMultiple`)
- A. James Clark School of Engineering (ENGR) (20)
- College of Agriculture & Natural Resources (AGNR) (17)
- College of Arts & Humanities (ARHU) (59)
- College of Behavioral & Social Sciences (BSOS) (20)
- College of Computer, Mathematical, & Natural Sciences (CMNS) (31)
- College of Education (EDUC) (16)
- College of Information (INFO) (6)
- Philip Merrill College of Journalism (JOUR) (1)
- Robert H. Smith School of Business (BMGT) (12)
- School of Architecture, Planning & Preservation (ARCH) (7)
- School of Public Health (SPH) (8)
- School of Public Policy (SPP) (6)

### 4. Explore by Interests (`interestCategories` → `categoryProgramInterest`)
- Art & Performance (18)
- Business & Entrepreneurship (41)
- Communication & Literature (42)
- Cultures & Languages (67)
- Data & Analysis (55)
- Design & Planning (26)
- Education & Human Development (31)
- Engineering & Technology (34)
- Environment & Natural Resources (41)
- Health & Wellness (33)
- Human Behavior & Social Thought (29)
- Natural & Physical Sciences (59)
- Plants & Animals (13)
- Policy & Social Justice (46)

### 5. Explore by Locations (`locationCategories` → `categoryProgramLocationMultiple`)
Note: only a subset of programs are tagged with a location; most inherit the default College Park campus.
- College Park (5)
- Shady Grove (12)

## Distinct type labels

`Major`, `Minor`, `Limited Enrollment Program`, `Certificate`, `Pre-Professional Program`. (The UI also mentions "Citation" conceptually, but **no** program in the current dataset carries a Citation label.)

## All programs (203)

College codes: ENGR, AGNR, ARHU, BSOS, CMNS, EDUC, INFO, JOUR, BMGT, ARCH, SPH, SPP. A dash (—) means no college was tagged on the entry.

| # | Name | Type / Labels | College | Letter | URL |
|---|------|---------------|---------|--------|-----|
| 1 | Accounting | Major, Limited Enrollment Program | BMGT | A | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 2 | Actuarial Mathematics | Minor | CMNS | A | https://www-math.umd.edu/undergraduate/math-minors.html |
| 3 | Advanced Cybersecurity Experience for Students | Minor | — | A | https://aces.umd.edu/minor |
| 4 | Aerospace Engineering | Major, Limited Enrollment Program | ENGR | A | https://aero.umd.edu/undergraduate/degrees/bachelor-science |
| 5 | African American Studies | Major, Certificate | BSOS | A | https://aasd.umd.edu/landing/Undergraduate |
| 6 | African Studies | Minor | BSOS | A | https://aasd.umd.edu/undergraduate/minor-african-studies |
| 7 | Agricultural & Resource Economics | Major | AGNR | A | https://agnr.umd.edu/academics/programs-study/agricultural-resource-economics |
| 8 | Agricultural Science & Technology | Major, Minor | AGNR | A | https://agnr.umd.edu/academics/programs-study/agricultural-science-technology |
| 9 | American Studies | Major | ARHU | A | https://amst.umd.edu/academic-programs/undergraduate |
| 10 | Animal Science | Major | AGNR | A | https://agnr.umd.edu/academics/programs-study/animal-science |
| 11 | Anthropology | Major | BSOS | A | https://anth.umd.edu/landing/Undergraduate |
| 12 | Anti-Black Racism | Minor | BSOS | A | https://aasd.umd.edu/undergraduate/minor-anti-black-racism-0 |
| 13 | Applied Agriculture | Certificate | AGNR | A | https://agnr.umd.edu/admissions/certificates |
| 14 | Arabic Studies | Major, Minor | ARHU | A | https://sllc.umd.edu/fields/arabic |
| 15 | Archaeology | Minor | ARHU | A | https://classics.umd.edu/academic-programs/minors/archaeology |
| 16 | Architecture | Major | ARCH | A | https://arch.umd.edu/programs/architecture/academics/architecture-degrees |
| 17 | Army Leadership Studies | Minor | — | A | https://armyrotc.umd.edu/minor-army-leadership-studies |
| 18 | Art Education | Major | EDUC | A | https://education.umd.edu/academics/programs/undergraduate/art-education-bachelor-arts-ba |
| 19 | Art History | Major, Minor | ARHU | A | https://arthistory.umd.edu/academics |
| 20 | Artificial Intelligence: Computational Structures for AI Systems | Major | CMNS | A | https://academiccatalog.umd.edu/undergraduate/colleges-schools/computer-mathematical-natural-sciences/computer-science/artificial-intelligence-computational-structures-ai-systems-major/ |
| 21 | Arts Leadership | Minor | ARHU | A | https://music.umd.edu/academic-programs/arts-leadership-minor |
| 22 | Asian American Studies | Minor | — | A | https://www.aast.umd.edu/aast-minor |
| 23 | Astronomy | Major, Minor | CMNS | A | https://www.astro.umd.edu/undergrad/ugprogram.html |
| 24 | Atmospheric & Oceanic Science | Major | CMNS | A | https://aosc.umd.edu/education/undergrad-major |
| 25 | Atmospheric Chemistry | Minor | CMNS | A | https://aosc.umd.edu/undergraduate/minor |
| 26 | Atmospheric Science | Minor | CMNS | A | https://aosc.umd.edu/undergraduate/minor |
| 27 | Biochemistry | Major, Limited Enrollment Program | CMNS | B | https://chem.umd.edu/undergraduate |
| 28 | Biocomputational Engineering | Major | ENGR | B | https://biocomp.umd.edu/ |
| 29 | Bioengineering | Major, Limited Enrollment Program | ENGR | B | https://bioe.umd.edu/undergraduate/bachelor-science |
| 30 | Biological Sciences | Major, Limited Enrollment Program | CMNS | B | https://bsci.umd.edu/about |
| 31 | Biomechanics and Motor Control | Minor | SPH | B | https://sph.umd.edu/academic-minors |
| 32 | Black Women's Studies | Minor | ARHU, BSOS | B | https://wgss.umd.edu/academic-programs/undergraduate/black-womens-studies-minor |
| 33 | Business Analytics | Minor | BMGT | B | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-minors |
| 34 | Chemical Engineering | Major, Limited Enrollment Program | ENGR | C | https://chbe.umd.edu/undergraduate/degrees/bachelor-science |
| 35 | Chemistry | Major, Limited Enrollment Program | CMNS | C | https://chem.umd.edu/undergraduate |
| 36 | Chinese | Major, Minor | ARHU | C | https://sllc.umd.edu/fields/chinese |
| 37 | Cinema & Media Studies | Major | ARHU | C | https://sllc.umd.edu/fields/cinema-media/major-ba |
| 38 | Civil Engineering | Major, Limited Enrollment Program | ENGR | C | https://cee.umd.edu/undergraduate/degrees/bachelor-science |
| 39 | Classical Mythology | Minor | ARHU | C | https://classics.umd.edu/academic-programs/minors/classical-mythology |
| 40 | Classics | Major | ARHU | C | https://classics.umd.edu/academic-programs/bachelor-arts |
| 41 | Communication | Major | ARHU | C | https://communication.umd.edu/academics/undergraduate/communication-BA |
| 42 | Computational Finance | Minor | BMGT, CMNS | C | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-minors |
| 43 | Computer Engineering | Major, Minor, Limited Enrollment Program | ENGR | C | https://ece.umd.edu/undergraduate/degrees |
| 44 | Computer Science | Major, Minor, Limited Enrollment Program | CMNS | C | https://undergrad.cs.umd.edu/future |
| 45 | Construction Project Management | Minor | ARCH, ENGR | C | https://pm.umd.edu/program/cpm-minor/ |
| 46 | Creative Placemaking | Minor | ARCH, ARHU | C | https://art.umd.edu/academic-programs/creative-placemaking-minor#:~:text=The%20minor%20is%2a%20collaboration,arts%2C%20technology%20and%20social%20justice. |
| 47 | Creative Writing | Minor | ARHU | C | https://english.umd.edu/academic-programs/undergraduate/english-minors#:~:text=The%20minor%20in%20creative%20writing,writers%20of%20poetry%20and%20prose |
| 48 | Criminology & Criminal Justice | Major, Minor, Limited Enrollment Program | BSOS | C | https://ccjs.umd.edu/landing/Undergraduate |
| 49 | Cyber-Physical Systems Engineering | Major, Limited Enrollment Program | ENGR | C | https://shadygrove.ece.umd.edu/ |
| 50 | Dance | Major | ARHU | D | https://tdps.umd.edu/academic-programs/ba-dance |
| 51 | Data Science | Minor | CMNS | D | https://academiccatalog.umd.edu/undergraduate/colleges-schools/computer-mathematical-natural-sciences/computer-science/data-science-minor/ |
| 52 | Demography | Minor | BSOS | D | https://socy.umd.edu/landingtopic/demography-minor |
| 53 | Digital Storytelling & Poetics | Minor | ARHU | D | https://english.umd.edu/academic-programs/undergraduate/english-minors#:~:text=The%20minor%20in%20creative%20writing,writers%20of%20poetry%20and%20prose |
| 54 | Disability Studies | Minor | EDUC | D | https://education.umd.edu/disability-studies-minor-0 |
| 55 | Early Childhood & Early Childhood Special Education | Major | EDUC | E | https://education.umd.edu/academics/programs/undergraduate/early-childhood-and-early-childhood-special-education-bachelor |
| 56 | Earth History | Minor | CMNS | E | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 57 | Earth Material Properties | Minor | CMNS | E | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 58 | East Asian Studies | Certificate | ARHU | E | https://history.umd.edu/academics/undergraduate/east-asian-certificate |
| 59 | Economics | Major | BSOS | E | https://www.econ.umd.edu/landing/Undergraduate |
| 60 | Electrical Engineering | Major, Limited Enrollment Program | ENGR | E | https://ece.umd.edu/undergraduate/degrees/bs-electrical-engineering |
| 61 | Elementary Education | Major | EDUC | E | https://education.umd.edu/academics/programs/undergraduate/elementary-education-bachelor-science-bs |
| 62 | Elementary/Middle Special Education | Major | EDUC | E | https://education.umd.edu/academics/programs/undergraduate/elementarymiddle-special-education-bachelor-science-bs |
| 63 | English | Major | ARHU | E | https://english.umd.edu/academic-programs/undergraduate/english-ba |
| 64 | Entomology | Minor | AGNR, CMNS | E | https://entomology.umd.edu/entomology-minor.html |
| 65 | Environmental Science & Policy | Major | AGNR, CMNS, BSOS | E | https://agnr.umd.edu/academics/programs-study/environmental-science-policy |
| 66 | Environmental Science & Technology | Major | AGNR | E | https://agnr.umd.edu/academics/programs-study/environmental-science-technology |
| 67 | Exercise Physiology | Minor | SPH | E | https://sph.umd.edu/academic-minors |
| 68 | Family Health | Major | SPH | F | https://sph.umd.edu/undergraduate-degrees/bs-family-health |
| 69 | Fermentation Science | Major | AGNR | F | https://nfsc.umd.edu/undergraduate/fermentation-science |
| 70 | Finance | Major, Limited Enrollment Program | BMGT | F | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 71 | Fire Protection Engineering | Major, Limited Enrollment Program | ENGR | F | https://fpe.umd.edu/undergraduate/degrees/bachelor-science |
| 72 | French Language & Literature | Major | ARHU | F | https://sllc.umd.edu/fields/french/undergraduate/major-ba |
| 73 | French Studies | Minor | ARHU | F | https://sllc.umd.edu/fields/french/undergraduate/minor |
| 74 | General Business | Minor | BMGT | G | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-minors |
| 75 | Geochemistry | Minor | CMNS | G | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 76 | Geographic Information Science | Minor | BSOS | G | https://geog.umd.edu/undergraduate/gis-minor |
| 77 | Geographical Sciences | Major | BSOS | G | https://geog.umd.edu/undergraduate/prospective-students |
| 78 | Geology | Major | CMNS | G | https://www.geol.umd.edu/undergraduate/whygeology.php |
| 79 | Geophysics | Minor | CMNS | G | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 80 | German Studies | Major, Minor | ARHU | G | https://sllc.umd.edu/fields/german/undergraduate |
| 81 | Global & Foreign Policy | Major | AGNR, ARHU, SPP | G | https://spp.umd.edu/your-education/undergraduate/bachelor-arts-global-and-foreign-policy |
| 82 | Global Engineering Leadership | Minor | ENGR | G | https://eng.umd.edu/global/coursework |
| 83 | Global Health | Major | SPH | G | https://sph.umd.edu/undergraduate-degrees/bs-global-health |
| 84 | Global Poverty | Minor | AGNR | G | https://www.arec.umd.edu/undergraduate/minor |
| 85 | Global Terrorism Studies | Minor | BSOS | G | https://www.start.umd.edu/education/global-terrorism-studies-minor-program |
| 86 | Government and Politics | Major | BSOS | G | https://gvpt.umd.edu/landing/Undergraduate |
| 87 | Greek Language & Culture | Minor | ARHU | G | https://classics.umd.edu/academic-programs/minors/greek-language-culture |
| 88 | Hearing & Speech Sciences | Major, Minor | BSOS | H | https://hesp.umd.edu/landing/Undergraduate |
| 89 | Hebrew Studies | Minor | ARHU | H | https://jewishstudies.umd.edu/academic-programs/undergraduate/hs-minor |
| 90 | History | Major, Minor | ARHU | H | https://history.umd.edu/academics/undergraduate |
| 91 | History & Theory of Architecture | Minor | ARCH | H | https://arch.umd.edu/programs/architecture/academics/architecture-degrees/history-and-theory-architecture-minor |
| 92 | Human Development | Major, Minor | EDUC | H | https://education.umd.edu/academics/programs/undergraduate/human-development-bachelor-science-bs |
| 93 | Humanities, Health & Medicine | Minor | ARHU | H | https://english.umd.edu/academic-programs/undergraduate/english-minors#:~:text=The%20minor%20in%20creative%20writing,writers%20of%20poetry%20and%20prose |
| 94 | Hydrology | Minor | CMNS | H | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 95 | Immersive Media Design | Major, Limited Enrollment Program | ARHU, CMNS | I | https://imd.umd.edu/about |
| 96 | Individual Studies Program | Major | — | I | https://ivsp.umd.edu/ |
| 97 | Information Risk Management, Ethics & Privacy | Minor | INFO | I | https://ischool.umd.edu/academics/bachelors-programs/bachelor-of-science-in-information-science-shady-grove/minors/ |
| 98 | Information Science | Major | INFO | I | https://ischool.umd.edu/academics/bachelors-programs/ |
| 99 | Information Systems | Major, Limited Enrollment Program | BMGT | I | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 100 | Innovation & Entrepreneurship | Minor | BMGT | I | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-minors |
| 101 | International Agriculture & Natural Resources | Certificate | AGNR | I | https://agnr.umd.edu/academics/programs-study/international-agriculture-and-natural-resources |
| 102 | International Business | Major, Limited Enrollment Program | BMGT | I | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 103 | International Development & Conflict Management | Minor | BSOS | I | https://cidcm.umd.edu/landing/MIDCM |
| 104 | Israel Studies | Minor | ARHU | I | https://jewishstudies.umd.edu/academic-programs/undergraduate/is-minor |
| 105 | Italian Language & Culture | Minor | ARHU | I | https://sllc.umd.edu/fields/italian/minor |
| 106 | Italian Studies | Major | ARHU | I | https://sllc.umd.edu/fields/italian/major |
| 107 | Japanese | Major, Minor | ARHU | J | https://sllc.umd.edu/fields/japanese |
| 108 | Jewish Studies | Major, Minor | ARHU | J | https://jewishstudies.umd.edu/academic-programs/undergraduate |
| 109 | Journalism | Major | JOUR | J | https://merrill.umd.edu/degrees-programs/bachelors-degree |
| 110 | Kinesiology | Major | SPH | K | https://sph.umd.edu/undergraduate-degrees/bs-kinesiology |
| 111 | Korean Studies | Minor | ARHU | K | https://sllc.umd.edu/fields/korean/minor |
| 112 | Landscape Architecture | Major | AGNR | L | https://agnr.umd.edu/academics/programs-study/landscape-architecture |
| 113 | Landscape Management | Minor | AGNR | L | https://psla.umd.edu/undergraduate/minors |
| 114 | Latin American & Caribbean Studies | Minor, Certificate | ARHU | L | https://lacs.umd.edu/academics/undergraduate |
| 115 | Latin Language & Literature | Minor | ARHU | L | https://classics.umd.edu/academic-programs/minors/latin-language-literature |
| 116 | Law & Society | Minor | BSOS | L | https://mlaw.umd.edu/programs/about-minor |
| 117 | Leadership Studies | Minor, Certificate | EDUC | L | https://education.umd.edu/leadership-studies-program |
| 118 | LGBTQ Studies | Minor, Certificate | ARHU | L | https://wgss.umd.edu/academic-programs/undergraduate/LGBTQ-minor |
| 119 | Linguistics | Major, Minor | ARHU | L | https://linguistics.umd.edu/academic-programs/undergraduate |
| 120 | Management | Major, Limited Enrollment Program | BMGT | M | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 121 | Marketing | Major, Limited Enrollment Program | BMGT | M | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 122 | Materials Science & Engineering | Major, Limited Enrollment Program | ENGR | M | https://mse.umd.edu/undergraduate/degrees/bachelor-science |
| 123 | Mathematics | Major, Minor | CMNS | M | https://www-math.umd.edu/undergraduate/math-majors.html |
| 124 | Mechanical Engineering | Major, Limited Enrollment Program | ENGR | M | https://enme.umd.edu/undergraduate/degrees/bachelor-science |
| 125 | Mechatronics Engineering | Major | ENGR | M | https://shadygrove.umd.edu/academics/degree-programs/bs-mechatronics-engineering |
| 126 | Meteorology | Minor | CMNS | M | https://aosc.umd.edu/undergraduate/minor |
| 127 | Middle School Education - Mathematics & Science | Major | EDUC | M | https://education.umd.edu/academics/programs/undergraduate/middle-school-mathematics-and-science-bachelor-science-bs |
| 128 | Music & Culture | Minor | ARHU | M | https://music.umd.edu/academic-programs/music-culture-minor |
| 129 | Music Education | Major | ARHU, EDUC | M | https://music.umd.edu/academic-programs/bachelor-of-music-education |
| 130 | Music Performance | Minor | ARHU | M | https://music.umd.edu/academic-programs/music-performance-minor |
| 131 | Music: Liberal Arts Program | Major | ARHU | M | https://music.umd.edu/academic-programs/bachelor-of-arts |
| 132 | Music: Professional Program | Major | ARHU | M | https://music.umd.edu/academic-programs/bachelor-of-music |
| 133 | Nanoscale Science & Technology | Minor | ENGR, CMNS | N | https://www.nanocenter.umd.edu/education/nano-minor/ |
| 134 | Neuroscience | Major, Minor, Limited Enrollment Program | CMNS, BSOS | N | https://neur.umd.edu/landing/Academics |
| 135 | Nonprofit Leadership & Social Innovation | Minor | SPP | N | https://spp.umd.edu/your-education/undergraduate/minors |
| 136 | Nuclear Engineering | Minor | ENGR | N | https://enme.umd.edu/undergraduate/degrees/minor-nuclear-engineering |
| 137 | Nutrition & Food Science | Major | AGNR | N | https://agnr.umd.edu/academics/programs-study/nutrition-food-science |
| 138 | Operations Management & Business Analytics | Major, Limited Enrollment Program | BMGT | O | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 139 | Paleobiology | Minor | CMNS | P | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 140 | Persian Studies | Major, Minor | ARHU | P | https://sllc.umd.edu/fields/persian/undergraduate |
| 141 | Philosophy | Major, Minor | ARHU | P | https://philosophy.umd.edu/academic-programs/undergraduate-program/philosophy-major |
| 142 | Philosophy, Politics & Economics | Major | ARHU | P | https://philosophy.umd.edu/academic-programs/undergraduate-program/philosophy-politics-and-economics-major |
| 143 | Physics | Major, Minor | CMNS | P | https://umdphysics.umd.edu/academics/undergraduate/ugrad-prospective-students.html |
| 144 | Planetary Science | Minor | CMNS | P | https://www.astro.umd.edu/undergrad/minorPlanSci.html |
| 145 | Plant Science | Major | AGNR | P | https://agnr.umd.edu/academics/programs-study/plant-science |
| 146 | Portuguese Language, Literature & Culture | Minor | ARHU | P | https://sllc.umd.edu/fields/portuguese/minor |
| 147 | Pre-Dental Hygiene | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/dental-hygiene |
| 148 | Pre-Dentistry | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/dentistry-2 |
| 149 | Pre-Genetic Counseling | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/genetic-counseling |
| 150 | Pre-Law | Pre-Professional Program | — | P | https://ltsc.umd.edu/prelaw |
| 151 | Pre-Medicine | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/medicine-2 |
| 152 | Pre-Nursing | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/nursing |
| 153 | Pre-Occupational Therapy | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/occupational-therapy |
| 154 | Pre-Optometry | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/optometry |
| 155 | Pre-Pharmacy | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/pharmacy |
| 156 | Pre-Physical Therapy | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/prephysicaltherapy |
| 157 | Pre-Physician Assistant | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/physician-assistant |
| 158 | Pre-Podiatry | Pre-Professional Program | — | P | https://www.prehealth.umd.edu/podiatry |
| 159 | Pre-Veterinary | Pre-Professional Program | — | P | https://agnr.umd.edu/information-prospective-pre-vet-students |
| 160 | Professional Writing | Minor | ARHU | P | https://english.umd.edu/academic-programs/undergraduate/english-minors#:~:text=The%20minor%20in%20creative%20writing,writers%20of%20poetry%20and%20prose |
| 161 | Project Management | Minor | ENGR, ARCH | P | https://pm.umd.edu/program/undergraduate-minor-in-project-management/ |
| 162 | Psychology | Major, Limited Enrollment Program | BSOS | P | https://psyc.umd.edu/landing/Undergraduate |
| 163 | Public Health Practice | Major | SPH | P | https://sph.umd.edu/undergraduate-degrees/bs-public-health-practice |
| 164 | Public Health Science | Major | SPH | P | https://sph.umd.edu/undergraduate-degrees |
| 165 | Public Leadership | Minor | SPP | P | https://spp.umd.edu/your-education/undergraduate/minors |
| 166 | Public Policy | Major | SPP | P | https://spp.umd.edu/your-education/undergraduate/public-policy-major |
| 167 | Real Estate & the Built Environment | Major | ARCH | R | https://arch.umd.edu/programs/real-estate-development/academics/real-estate-development-degrees/bachelor-arts-real-estate-and-built-environment |
| 168 | Real Estate Development | Minor | ARCH | R | https://arch.umd.edu/programs/real-estate-development/academics/real-estate-development-degrees/real-estate-development-minor |
| 169 | Religions of the Ancient Middle East | Major | ARHU | R | https://jewishstudies.umd.edu/academic-programs/undergraduate/rame-ba |
| 170 | Religious Studies | Minor | ARHU | R | https://jewishstudies.umd.edu/academic-programs/undergraduate/rs-minor |
| 171 | Remote Sensing of Environmental Change | Minor | BSOS | R | https://geog.umd.edu/undergraduate/remote-sensing-minor |
| 172 | Rhetoric | Minor | ARHU | R | https://english.umd.edu/academic-programs/undergraduate/english-minors#:~:text=The%20minor%20in%20creative%20writing,writers%20of%20poetry%20and%20prose |
| 173 | Robotics & Autonomous Systems | Minor | ENGR, CMNS | R | https://robotics.umd.edu/minor |
| 174 | Romance Languages | Major | ARHU | R | https://sllc.umd.edu/fields/romance-languages |
| 175 | Russian Language & Literature | Major | ARHU | R | https://sllc.umd.edu/fields/russian/major |
| 176 | Russian Studies | Minor | ARHU | R | https://sllc.umd.edu/fields/russian/minor |
| 177 | Science, Technology, Ethics & Policy | Minor | ENGR, SPP, INFO | S | https://spp.umd.edu/your-education/undergraduate/minors/science-technology-ethics-and-policy-step-minor |
| 178 | Second Language Education | Minor | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/minor-second-language-education |
| 179 | Secondary Education | Minor | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/secondary-education-minor |
| 180 | Secondary Education - English | Major | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/secondary-education-bachelor-arts-ba-english-area-concentration |
| 181 | Secondary Education - Mathematics | Major | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/secondary-education-bachelor-science-bs-mathematics-terrapin |
| 182 | Secondary Education - Science | Major | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/secondary-education-bachelor-science-bs-science-terrapin-teachers |
| 183 | Secondary Education - Social Studies | Major | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/secondary-education-bachelor-arts-ba-or-bachelor-science-bs-social |
| 184 | Secondary Education - World Languages | Major | EDUC | S | https://education.umd.edu/academics/programs/undergraduate/secondary-education-bachelor-arts-ba-world-languages-area |
| 185 | Social Data Science | Major | INFO | S | https://sdsc.umd.edu/about-us/overview-0 |
| 186 | Sociology | Major, Minor | BSOS | S | https://socy.umd.edu/landing/Undergraduate |
| 187 | Soil Science | Minor | AGNR | S | https://enst.umd.edu/undergraduate/majors-minors |
| 188 | Spanish Heritage Language & Latina/o Culture | Minor | ARHU | S | https://sllc.umd.edu/fields/spanish/undergraduate/minor |
| 189 | Spanish Language, Culture & Professional Contexts | Minor | ARHU | S | https://sllc.umd.edu/fields/spanish/undergraduate/minor |
| 190 | Spanish Language, Literatures & Culture | Major | ARHU | S | https://sllc.umd.edu/fields/spanish/undergraduate/major |
| 191 | Spanish Literature, Linguistics & Culture | Minor | ARHU | S | https://sllc.umd.edu/fields/spanish/undergraduate/minor |
| 192 | Sport, Commerce & Culture | Minor | SPH | S | https://sph.umd.edu/academic-minors |
| 193 | Statistics | Minor | CMNS | S | https://www-math.umd.edu/undergraduate/math-minors.html |
| 194 | Studio Art | Major | — | S | https://art.umd.edu/academic-programs/studio-art-ba |
| 195 | Supply Chain Management | Major, Limited Enrollment Program | BMGT | S | https://www.rhsmith.umd.edu/programs/undergraduate/academics/academic-majors |
| 196 | Surficial Geology | Minor | CMNS | S | https://www.geol.umd.edu/undergraduate/Geology_Minors.php |
| 197 | Sustainability Studies | Minor | AGNR, SPP | S | https://agnr.umd.edu/sustainability-studies-minor |
| 198 | Technology & Information Design | Major | INFO | T | https://ischool.umd.edu/academics/bachelors-programs/bachelor-of-arts-in-technology-and-information-design-at-college-park/ |
| 199 | Technology Entrepreneurship & Corporate Innovation | Minor | ENGR | T | https://www.mtech.umd.edu/learning/minor-in-technology-entrepreneurship |
| 200 | Technology Innovation Leadership | Minor | INFO | T | https://ischool.umd.edu/academics/bachelors-programs/bachelor-of-science-in-information-science-shady-grove/minors/ |
| 201 | Theatre | Major | ARHU | T | https://tdps.umd.edu/academic-programs/ba-theatre |
| 202 | U.S. Latina/o Studies | Minor | ARHU | U | https://amst.umd.edu/academic-programs/undergraduate/us-latina-o-studies-minor |
| 203 | Women, Gender, & Sexuality Studies | Major, Certificate | ARHU | W | https://wgss.umd.edu/academic-programs/undergraduate |
