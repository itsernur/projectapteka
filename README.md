# Pharmacy Chain Website: Medicine Availability

A website for a pharmacy chain. Visitors search for a medicine and see which pharmacies have it in stock and how many units are available. Pharmacists and administrators keep the stock up to date through a simple dashboard or by uploading a file.

> Status: in development

## Features

- Search medicines by name or active ingredient
- View availability and quantity in every pharmacy of the chain
- Pharmacy list and map with address, phone number, and opening hours
- Filters: city, pharmacy, "in stock only", prescription / over-the-counter
- Pharmacist dashboard: update stock for your own pharmacy only
- Admin panel: manage pharmacies, medicines, and users
- Bulk stock upload from CSV / Excel
- "Last updated" timestamp for every stock record, so visitors know how fresh the information is

## User Roles

| Role | Permissions |
|---|---|
| Visitor | Search medicines, view availability, browse the pharmacy map |
| Pharmacist | Edit stock for their own pharmacy |
| Administrator | Full access to pharmacies, medicines, users, and stock |

## Tech Stack

Adjust this section to your own choices. A suggested setup:

- **Backend:** Node.js (Express / NestJS) or Python (FastAPI / Flask)
- **Frontend:** React / Next.js or plain HTML, CSS, and JavaScript
- **Maps:** Leaflet with OpenStreetMap
- **Search:** client-side or server-side filtering with fuzzy matching (for example, Fuse.js)
- **Deployment:** Docker, GitHub Actions for CI/CD

## Project Structure

```
.
├── src/                # application source code
├── public/             # static assets (images, icons)
├── scripts/            # helper scripts (validation, import)
├── docs/               # documentation and mockups
├── .env.example
└── README.md
```

## Getting Started

### Requirements

- Git
- Node.js 20+ (or Python 3.11+ if you use a Python backend)
- Docker and Docker Compose (optional)

### Installation

```bash
git clone <REPOSITORY_URL>
cd <project-folder>
cp .env.example .env
npm install
```

Fill in `.env`:

```env
PORT=3000
SECRET_KEY=replace_with_your_own_key
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=change_me
```

### Run locally

```bash
npm run dev
```

Open `http://localhost:3000` in your browser.

### Run with Docker

```bash
docker compose up --build
```

### Build for production

```bash
npm run build
npm start
```

## Updating Stock

There are three ways to keep availability up to date, from simplest to most automated:

1. **Manually** through the pharmacist dashboard or the admin panel.
2. **File upload** in CSV or Excel format, once a day or more often. Example:

   ```csv
   pharmacy_id,medicine_id,quantity,price
   1,105,24,350.00
   1,212,0,120.50
   2,105,8,355.00
   ```

3. **Automatic sync** with your accounting system (for example, 1C) through an API or a scheduled export (cron).

Rules for stock records:

- One row is one medicine in one pharmacy
- `quantity` must be an integer of 0 or more
- `pharmacy_id` and `medicine_id` must refer to existing pharmacies and medicines
- Duplicate `pharmacy_id` + `medicine_id` pairs are not allowed

Always show the date of the last update next to the quantity.

## Testing

```bash
npm test
```

What the tests cover:

- Stock logic (quantity never goes below zero)
- Search and filters
- Role-based access (a pharmacist can edit only their own pharmacy)
- File upload and validation
- Mobile layout checks and a basic load test of the search

## Security

- Passwords are stored only as hashes
- HTTPS is used in production
- Protection against injection attacks and XSS
- Role-based access control
- Regular backups of all project files
- If you collect personal data (reservations, orders), follow your country's personal data laws

## Legal Notes

Before launch, check your country's rules on publishing information about medicines online: showing and reserving prescription drugs, advertising restrictions, and personal data processing.

## Roadmap

- [ ] Requirements and mockups
- [ ] Pharmacy and medicine catalog
- [ ] Search with suggestions and filters
- [ ] Pharmacist dashboard and admin panel
- [ ] CSV / Excel stock upload with validation
- [ ] Public website and map
- [ ] Authentication and roles
- [ ] Tests and CI/CD
- [ ] Deployment, domain, and SSL
- [ ] Medicine reservation
- [ ] "Back in stock" notifications
- [ ] Integration with the accounting system
- [ ] Mobile app, online payment, analogs of medicines

## Contributing

1. Create a branch: `git checkout -b feature/your-feature`
2. Make your changes and add tests
3. Commit: `git commit -m "Describe your changes"`
4. Push the branch and open a Pull Request

## License

Specify a license (for example, MIT) or state that the code is proprietary.

## Contact

- Author: Shyngys Rustemuly,Ernur Zhubandyk
