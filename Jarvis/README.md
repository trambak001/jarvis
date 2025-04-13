# Jarvis Virtual Assistant

A Python-based virtual assistant with voice recognition and various utility functions.

## Features

- Voice recognition and text-to-speech
- Web search capabilities
- System control (volume, brightness)
- Weather information
- Alarm functionality
- Application control
- Wikipedia search
- Time and date information

## Security Considerations

1. **Input Validation**: All user inputs are validated to prevent command injection attacks.
2. **Safe Application Control**: Only allows opening/closing of whitelisted applications.
3. **Error Handling**: Comprehensive error handling and logging implemented.
4. **Web Requests**: Timeouts and error handling for web requests.
5. **File Operations**: Safe file handling with proper error checking.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jarvis.git
cd jarvis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python alexapy.py
```

## Logging

The application logs all activities and errors to `jarvis.log`. Check this file for debugging information.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 