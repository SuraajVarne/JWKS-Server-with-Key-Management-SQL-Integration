# JWKS Server with Key Management and SQL Integration

## Overview

This project implements a RESTful JWKS Server in Python that efficiently manages RSA key pairs and handles secure token management. The server offers rapid access to public keys and JSON Web Tokens (JWTs) with robust security and performance optimizations.

## Features

- **RSA Key Management:** 
  - Manages over 100 RSA keys.
  - Handles over 200 requests for public keys and JWTs.
  - Reduced response time for key retrieval by 40%.
  
- **Key Storage with SQLite:**
  - Secure storage of 20 RSA keys in SQLite.
  - Achieves 95% query efficiency for token management.

- **User Authentication:**
  - Includes user authentication features.
  - Processes over 50 user registrations for an improved security experience.

## Technologies Used

- Python
- Flask (for the REST API)
- SQLite (for key storage)
- JWT (JSON Web Token)
- RSA Encryption

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/SuraajVarne/JWKS-Server-with-Key-Management-SQL-Integration.git
