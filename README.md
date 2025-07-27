# 🔗 Flask REST API - Task Manager

A complete RESTful API built with Python Flask implementing full CRUD operations for task management. Features standardized HTTP methods, JSON data handling, and comprehensive endpoint testing through Postman integration, demonstrating modern backend development practices.

## 📸 Preview

```json
POST /tasks
{
    "title": "Estudar Flask",
    "description": "Aprender desenvolvimento de APIs REST"
}

GET /tasks
{
    "tasks": [
        {
            "id": 1,
            "title": "Estudar Flask",
            "description": "Aprender desenvolvimento de APIs REST",
            "completed": false
        }
    ],
    "total_tasks": 1
}
```

## 📋 About This Project

This project is a comprehensive REST API implementation using Flask framework, demonstrating modern backend development practices through a task management system. The API provides complete CRUD functionality with proper HTTP methods, JSON data handling, and standardized response formats, designed for testing and integration with frontend applications or API clients.

### Core API Features:
- **RESTful Design** - Standard HTTP methods and resource-based URLs
- **CRUD Operations** - Complete Create, Read, Update, Delete functionality
- **JSON Communication** - Standardized request/response data format
- **Error Handling** - Proper HTTP status codes and error messages
- **Postman Integration** - Comprehensive API testing and documentation
- **Modular Architecture** - Separated models and routing logic

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Flask Framework** - Lightweight web framework for API development
  - **Flask routing** - HTTP method handling and URL mapping
  - **JSON handling** - Request parsing and response formatting
  - **Error management** - HTTP status codes and error responses
- **Postman** - API testing and endpoint validation
- **Object-Oriented Design** - Task model with proper encapsulation

## 🎯 API Endpoints

### **Create Task**
- **Method:** `POST /tasks`
- **Body:** `{"title": "Task name", "description": "Task details"}`
- **Response:** Success message with task creation confirmation

### **Get All Tasks**
- **Method:** `GET /tasks`
- **Response:** JSON array with all tasks and total count

### **Get Specific Task**
- **Method:** `GET /tasks/<id>`
- **Response:** Single task object or 404 error if not found

### **Update Task**
- **Method:** `PUT /tasks/<id>`
- **Body:** `{"title": "New title", "description": "New description", "completed": true}`
- **Response:** Success message or 404 error if not found

### **Delete Task**
- **Method:** `DELETE /tasks/<id>`
- **Response:** Success message or 404 error if not found

## 🔧 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/xManoelx/flask-task-api.git
   cd flask-task-api
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the API server**
   ```bash
   python app.py
   ```

4. **Test with Postman**
   - Import API collection
   - Test all CRUD endpoints
   - Validate responses and error handling

## 🏗️ API Architecture

### **Flask Application Structure:**
- **Route Definitions** - HTTP method mapping and URL patterns
- **Request Processing** - JSON data parsing and validation
- **Business Logic** - Task manipulation and data management
- **Response Formatting** - Standardized JSON responses

### **Task Model:**
- **Data Structure** - ID, title, description, completion status
- **Serialization** - `to_dict()` method for JSON conversion
- **Validation** - Input data verification and error handling

### **Data Management:**
- **In-Memory Storage** - List-based task storage for development
- **ID Control** - Auto-incrementing task identification
- **CRUD Operations** - Complete data manipulation functionality

## 📊 HTTP Status Codes

- **200 OK** - Successful GET, PUT operations
- **201 Created** - Successful POST operations
- **404 Not Found** - Task not found for specified ID
- **400 Bad Request** - Invalid request data format

## 🧪 Testing with Postman

### **Test Scenarios:**
1. **Create new tasks** with valid and invalid data
2. **Retrieve all tasks** and verify response format
3. **Get specific tasks** by ID with existing and non-existing IDs
4. **Update tasks** with partial and complete data
5. **Delete tasks** and verify removal from collection

### **Validation Points:**
- **Response Format** - JSON structure and data types
- **Error Handling** - Proper HTTP status codes
- **Data Persistence** - Verify operations affect task list
- **Edge Cases** - Invalid IDs, missing data, malformed requests

## 📚 What I Learned

This project enhanced my backend development skills in:

- **REST API Design** - Understanding RESTful principles and conventions
- **Flask Framework** - Building web APIs with Python's lightweight framework
- **HTTP Protocol** - Proper use of methods, status codes, and headers
- **JSON Data Handling** - Parsing requests and formatting responses
- **API Testing** - Using Postman for comprehensive endpoint validation
- **Error Handling** - Implementing proper error responses and status codes
- **Backend Architecture** - Separating concerns between models and routes

## 🌟 Technical Highlights

- **RESTful Design** - Following REST conventions for resource management
- **Proper HTTP Methods** - Correct usage of GET, POST, PUT, DELETE
- **JSON Serialization** - Custom `to_dict()` methods for object conversion
- **Error Handling** - Comprehensive 404 handling and validation
- **Modular Code** - Clean separation between routing and business logic
- **Development Ready** - Debug mode enabled for development testing

## 🚀 Backend Development Concepts

- **API Design Patterns** - RESTful resource management
- **Request/Response Cycle** - Understanding HTTP communication
- **Data Serialization** - Converting objects to JSON format
- **Route Parameters** - Dynamic URL handling with Flask
- **Global State Management** - Managing application-level variables

## 🔄 Future Improvements

- [ ] Add database integration (SQLite, PostgreSQL)
- [ ] Implement user authentication and authorization
- [ ] Add input validation and sanitization
- [ ] Create API documentation with Swagger
- [ ] Add pagination for large task collections
- [ ] Implement filtering and search functionality
- [ ] Add task categories and priority levels

## 👨‍💻 Author

**Manoel Antonio**
- Junior Robot Programmer transitioning to Full Stack Development
- GitHub: [@xManoelx](https://github.com/xManoelx)
- Location: Caxias do Sul, RS, Brasil

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*From industrial robotics to REST API development - building the backend foundation for modern web applications! 🤖🔗*
