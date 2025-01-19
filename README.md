# Booking System (MVP)

A Django-based (for the moment) booking system for managing appointments. The system is modular, allowing users to define their own services and workflows without altering the core structure.

---

## The App

### Overview
The Booking System enables:
- **Clients**: Book one or multiple services, view pricing, and manage their bookings via a unique link.
- **Providers**: Add and manage services, set availability slots, and oversee client bookings.

---

## Installation

### Clone the repository
```bash
git clone https://github.com/FastAce/booking-system.git
cd booking-system
```

### Create a virtual environment (optional)
#### Create the environment:
```bash
python -m venv env
```

#### Activate it:
- **Windows**:
  ```bash
  .\\env\\Scripts\\activate
  ```
- **Linux/Mac**:
  ```bash
  source env/bin/activate
  ```

#### Install required Python packages:
```bash
pip install -r requirements.txt
```

---

## Running the Application

### Apply migrations:
```bash
python manage.py migrate
```

### Start the Django development server:
```bash
python manage.py runserver
```

### Access the application:
Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

### For Providers
1. Log in to the Django admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
2. Add your services (e.g., manicure, car repair).
3. Set availability for bookings.
4. Manage bookings made by clients.

### For Clients
1. Access the booking system at [http://127.0.0.1:8000](http://127.0.0.1:8000).
2. Browse and select one or multiple services.
3. Choose a date and time slot.
4. Confirm your booking and receive a link to manage it.

---

## Development

### Project Structure
The project follows a standard Django structure:
- **booking_system**: Core Django project files.
- **booking**: Application folder for managing services, availability, and bookings.
- **templates**: HTML templates for views (future addition).
- **static**: Static files like CSS and JS (future addition).

---

## Running Tests
Run the unit tests:
```bash
python manage.py test
```

---

## Contribution

Contributions are welcome! 🎉

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add meaningful commit message"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request on GitHub.

---

## TO-DO

### **Core Features**
- [ ] Create the models:
  - [ ] \`Service\`: To manage the services offered by providers.
  - [ ] \`Availability\`: To manage the providers' time slots.
  - [ ] \`Booking\`: To handle client bookings.
- [ ] Build the booking API:
  - [ ] Endpoint for clients to create a booking.
  - [ ] Endpoint for clients to cancel or view their booking.
  - [ ] Endpoint for providers to manage availability.
- [ ] Set up the Django admin for providers:
  - [ ] Add, edit, or remove services.
  - [ ] Manage availability slots.
- [ ] Test the booking workflow (end-to-end).

### **Frontend (Future Step)**
- [ ] Design a simple frontend (e.g., React or plain HTML/CSS):
  - [ ] Clients can browse services and book.
  - [ ] Providers can manage availability.
- [ ] Integrate the frontend with the Django backend.

### **Improvements**
- [ ] Add email notifications for:
  - [ ] Booking confirmation.
  - [ ] Booking cancellation.
- [ ] Improve the UI/UX for better navigation.

### **Documentation**
- [ ] Write clear instructions for:
  - [ ] Setting up the project.
  - [ ] Adding custom services.
  - [ ] Managing bookings and availability.
- [ ] Add examples for using the APIs.

---
Feel free to contribute to this project by working on any of the tasks above!

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

