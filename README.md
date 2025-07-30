# Kanban Board API

A RESTful API for managing Kanban boards built with FastAPI, following Test-Driven Development (TDD), SOLID principles, and Domain-Driven Design (DDD).

## 🚀 Features

- **Board Management**: Create and retrieve Kanban boards
- **Column Management**: Add columns to boards with validation
- **OpenAPI Compliant**: Full OpenAPI 3.0 specification support
- **100% Test Coverage**: Comprehensive test suite with pytest
- **Error Handling**: Proper HTTP status codes and error responses
- **Type Safety**: Full Pydantic model validation

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **pytest**: Testing framework with coverage reporting
- **Python 3.11+**: Latest Python features and performance

## 📋 API Endpoints

### Boards
- `POST /api/v1/boards` - Create a new board
- `GET /api/v1/boards/{board_id}` - Retrieve a board by ID

### Columns
- `POST /api/v1/boards/{board_id}/columns` - Add a column to a board

## 🏗️ Project Structure

```
kanban_backend/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI app with all endpoints
├── tests/
│   └── test_kanban.py       # Comprehensive test suite
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚦 Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cards
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   # source .venv/bin/activate    # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive API Docs: `http://localhost:8000/docs`
   - OpenAPI Schema: `http://localhost:8000/openapi.json`

## 🧪 Testing

### Run Tests with Coverage
```bash
export PYTHONPATH=/path/to/project  # Set Python path
pytest tests/test_kanban.py --cov=app --cov-report=term-missing -v
```

### Current Test Coverage
- **100% Code Coverage** across all modules
- **5 Test Cases** covering positive and negative scenarios
- **Comprehensive Error Handling** validation

### Test Cases
1. `test_create_board` - Board creation
2. `test_add_column_to_board` - Column addition to existing board
3. `test_get_board_by_id` - Board retrieval by ID
4. `test_get_nonexistent_board` - 404 handling for missing boards
5. `test_add_column_to_nonexistent_board` - Validation for non-existent boards

## 📖 API Usage Examples

### Create a Board
```bash
curl -X POST "http://localhost:8000/api/v1/boards" \
     -H "Content-Type: application/json" \
     -d '{"name": "My Project Board"}'
```

### Get a Board
```bash
curl -X GET "http://localhost:8000/api/v1/boards/{board_id}"
```

### Add a Column
```bash
curl -X POST "http://localhost:8000/api/v1/boards/{board_id}/columns" \
     -H "Content-Type: application/json" \
     -d '{"name": "To Do"}'
```

## 🏛️ Architecture & Design Principles

### Test-Driven Development (TDD)
- **Red-Green-Refactor**: Write failing tests first, implement minimal code, then refactor
- **100% Coverage**: Every line of code is tested
- **Pytest Fixtures**: Clean test setup without assertions in setup code

### SOLID Principles
- **Single Responsibility**: Each function has one clear purpose
- **Open/Closed**: Code is open for extension, closed for modification
- **Interface Segregation**: Clean API contracts with Pydantic models
- **Dependency Inversion**: Abstractions over concrete implementations

### Domain-Driven Design (DDD)
- **Domain Models**: Board, Column, and Card entities
- **Aggregates**: Board as the root aggregate containing columns
- **Value Objects**: Proper typing with Pydantic models

## 🔮 Future Enhancements

- **Card Management**: Add, edit, and move cards between columns
- **Persistence Layer**: Database integration (PostgreSQL/MongoDB)
- **Authentication**: User management and board permissions
- **Real-time Updates**: WebSocket support for live collaboration
- **Tameflow Integration**: Advanced Kanban concepts from Steve Tendon's work
- **Metrics & Analytics**: Flow metrics and performance tracking

## 🤝 Development Workflow

1. **Write Test First**: Always start with a failing test
2. **Implement Minimal Code**: Write just enough to make the test pass
3. **Refactor**: Improve code quality while keeping tests green
4. **Validate Coverage**: Ensure 100% test coverage is maintained
5. **OpenAPI Compliance**: All endpoints follow OpenAPI 3.0 standards

## 📝 Contributing

1. Follow TDD practices - tests first, then implementation
2. Maintain 100% test coverage
3. Use proper Pydantic models for all API contracts
4. Follow OpenAPI specification standards
5. Update documentation for new features

## 📄 License

This project is developed for educational purposes following modern software engineering practices.