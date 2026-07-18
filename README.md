
# 🤖 AI Email Research Assistant

![Python](https://img.shields.io/badge/Python-3.14%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![DigitalOcean](https://img.shields.io/badge/Hosted%20on-DigitalOcean-0080FF)

An AI-powered multi-agent application built with **FastAPI**, **LangGraph**, and **OpenAI** that researches a topic, prepares an email, and sends the results automatically.

---

# ✨ Features

- 🧠 Multi-agent orchestration using LangGraph Supervisor
- 🔎 Dedicated research agent
- 📧 Dedicated email agent
- 🤖 OpenAI-powered research and summarization
- ⚡ FastAPI REST API
- 🐳 Dockerized development environment
- 🗄️ PostgreSQL integration
- ☁️ Deployable to DigitalOcean App Platform

---

# 🏗️ Architecture

```text
                 User
                   │
                   ▼
            FastAPI Endpoint
                   │
                   ▼
         LangGraph Supervisor
          ┌────────┴────────┐
          ▼                 ▼
   Research Agent     Email Agent
          │                 │
          ▼                 ▼
 Research Tool       Email Tools
          │
          ▼
      OpenAI Model
```

## Agent Workflow

```text
User Request
      │
      ▼
Supervisor
      │
      ├──► Research Agent
      │         │
      │         ▼
      │   Research + Email Draft
      │
      └──► Email Agent
                │
                ▼
          Send Email
                │
                ▼
        Success Response
```

---

# 📁 Project Structure

```text
backend/
├── src/
│   ├── api/
│   │   ├── ai/
│   │   │   ├── agents.py
│   │   │   ├── assistants.py
│   │   │   ├── tools.py
│   │   │   └── schemas.py
│   │   ├── chat/
│   │   └── myemailer/
│   ├── main.py
│   └── ...
├── requirements.txt
└── Dockerfile
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.14
- Docker & Docker Compose
- OpenAI API key
- Gmail App Password (if using Gmail)
- PostgreSQL

## Clone

```bash
git clone https://github.com/Manpreeth07/docker-ai-agent-python.git
cd docker-ai-agent-python
```

## Environment Variables

Copy the sample environment file:

```bash
cp .env.sample .env
```

Configure values such as:

```env
OPENAI_API_KEY=your_openai_api_key

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password

DATABASE_URL=postgresql+psycopg://username:password@db:5432/database
```

---

# 🐳 Run with Docker

```bash
docker compose build
docker compose up
```

API:

```
http://localhost:8080
```

Swagger UI:

```
http://localhost:8080/docs
```

---

# 📬 API Example

Request

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message":"Research the benefits of going outside and email me the results"}' \
http://localhost:8080/api/chats/
```

Example Response

```json
{
  "content": "I've completed your request. The email containing the research has been sent."
}
```

---

# ☁️ Deploying to DigitalOcean

1. Push the repository to GitHub.
2. Create a new App Platform application.
3. Connect the GitHub repository.
4. Attach a managed PostgreSQL database.
5. Configure environment variables.
6. Deploy the application.

---

# 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| AI | LangGraph, LangChain, OpenAI |
| Database | PostgreSQL |
| Containerization | Docker |
| Deployment | DigitalOcean App Platform |

---

# 🗺️ Roadmap

- [ ] Persistent conversation memory
- [ ] User authentication
- [ ] Streaming responses
- [ ] Web frontend
- [ ] Additional research tools
- [ ] CI/CD with GitHub Actions
- [ ] Unit and integration tests

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👤 Author

**Manpreeth**

If you found this project useful, consider giving it a ⭐ on GitHub.
