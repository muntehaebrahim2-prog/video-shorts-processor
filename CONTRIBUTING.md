# Contributing to Video Shorts Processor

Thank you for your interest in contributing! Here are some guidelines to help you get started.

## Code of Conduct

Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. Provide detailed description of the bug
3. Include steps to reproduce
4. Add relevant logs or error messages
5. Specify your Python version and OS

### Suggesting Enhancements

1. Check if the feature has been requested
2. Provide clear description of the feature
3. Explain the use case and benefits
4. Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Submit a pull request

## Development Setup

```bash
# Clone repository
git clone https://github.com/muntehaebrahim2-prog/video-shorts-processor.git
cd video-shorts-processor

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Install pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

## Code Style

- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and modular

## Testing

Before submitting a PR:

```bash
# Run tests
pytest tests/ -v

# Check coverage
pytest tests/ --cov=src
```

## Commit Messages

Use clear, descriptive commit messages:

```
Fix: Correct video resize issue
Feature: Add watermark support
Docs: Update configuration guide
Test: Add video processor tests
```

## Questions?

Feel free to open an issue for discussions or questions!

---

Thank you for contributing! 🎉
