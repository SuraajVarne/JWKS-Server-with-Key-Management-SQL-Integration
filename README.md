# JWKS Server with Key Management and User Authentication

## Overview

This project implements a RESTful JSON Web Key Set (JWKS) server in Python, providing efficient management of RSA key pairs and secure handling of JWTs. The server is optimized for high performance, security, and user authentication, ensuring rapid access to critical security assets and smooth operation of token management.

### Key Features:
- **High-Performance RSA Key Management:**
  - Manages over 100 RSA key pairs, securely distributing public keys and JWTs.
  - Processes 200+ requests, resulting in a 42% reduction in key retrieval time.

- **Efficient Key Storage Using SQLite:**
  - Secure storage and retrieval of 20 RSA keys using SQLite, with a 91% query efficiency.
  - Strong security protocols to safeguard token-related data.

- **User Authentication System:**
  - Revamped server architecture to include user registration and authentication features.
  - Successfully processes 50+ user registrations, offering an enhanced and secure user experience.

---

## Technologies Used

- **Python**: Core language for implementing the server logic.
- **Flask**: Lightweight Python framework for creating RESTful APIs.
- **SQLite**: Database used to securely store and manage RSA keys.
- **JWT**: JSON Web Token for secure authentication and authorization.
- **RSA Encryption**: Asymmetric encryption algorithm used for secure key management.

---

## Project Structure

Here is the key architecture of the project:

1. **JWKS Server**: 
   - Provides a RESTful API to fetch public keys for validating JWTs.
   - Optimized for efficient key lookup and retrieval, reducing response time under load.

2. **Key Management System**: 
   - Utilizes SQLite for storing RSA keys securely.
   - Optimized queries ensure fast access to keys, even as the dataset grows.

3. **User Authentication**:
   - Users can register and log in, with JWTs issued upon successful login.
   - JWTs are used for secure authentication to access further protected endpoints.

---

## Running the Project Locally

### Prerequisites:
- Python 3.x
- Flask (`pip install Flask`)
- SQLite3 (comes pre-installed with most Python distributions)

### Steps to Run:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SuraajVarne/JWKS-Server-with-Key-Management-SQL-Integration.git


## Running the Project Locally

### Navigate to the project directory:
```bash
cd JWKS-Server-with-Key-Management-SQL-Integration

