# OWN GPT Using Amazon Web Services (AWS) Bedrock

## Description
I've harnessed the power of AWS Bedrock to create a versatile AI platform that delivers:
- 📝 **Text Generation (Meta.llama2):** Engaging and coherent conversations like ChatGPT.
- 🎨 **Image Generation (Stability.AI's Stable Diffusion):** Stunning visuals from text prompts, inspired by MidJourney.
- 💻 **Code Generation (Anthropic.claude):** Efficient code solutions, similar to CodeX.

Key technologies driving this project include Meta.llama2, Stability.AI's Stable Diffusion, and Anthropic.claude. I've developed a sleek web interface using Streamlit for easy public access.

## Repository Structure
This repository contains the following files:

- `imageGen.py`: Code for Image Generation.
- `textGen.py`: Code for Text Generation.
- `codeGen.py`: Code for Code Generation.
- `app.py`: Streamlit web application for user interaction.
- `requirements.txt`: List of required Python packages.

## Getting Started

### Prerequisites
To run this project, you'll need the following installed on your system:
- Python 3.8+
- AWS account with Bedrock access
- Streamlit
- Required Python packages (listed in `requirements.txt`)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/own-gpt-aws-bedrock.git
    cd own-gpt-aws-bedrock
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure AWS credentials:
    Set up your AWS credentials to access the IAM user role:
    ```sh
    aws configure
    ```
    - AWS Access Key ID: [Enter your access key ID]
    - AWS Secret Access Key: [Enter your secret access key]
    - Default region name: `us-east-1`
    - Default output format: `json`

### Running the Application
To start the Streamlit application, run:
```sh
streamlit run app.py
```

This will open the web interface in your default browser.

## Preview
![Streamlit App Preview](https://github.com/Surendraprajapat18/OWN-GPT-Using-Amazon-Web-Services-AWS-Bedrock/assets/97840357/cd1de042-e018-4ccf-9867-4cf8f8ce5268)

## Demo Video

Uploading GPTUsingBedrock - Made with Clipchamp.mp4…


## Usage
- **Text Generation:** Enter text prompts to generate engaging and coherent conversations.
- **Image Generation:** Input text prompts to create stunning visuals.
- **Code Generation:** Provide coding tasks to receive efficient code solutions.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
