# Material Components for Slint Python Template

A template for a Python Application using Slint with [material components](https://github.com/slint-ui/slint/tree/master/ui-libraries/material). Based on the material gallery. 

## About

This template helps you get started developing a Rust application with Slint as a toolkit
for the user interface and the material component set. It demonstrates the integration between the `.slint`
UI markup and Python code, how to react to callbacks, get and set properties, and use of all available
material components for Slint.

## Usage

We recommend using an IDE for development, along with our [LSP-based IDE integration for `.slint` files](https://github.com/slint-ui/slint/blob/master/tools/lsp/README.md). You can also load this project directly in [Visual Studio Code](https://code.visualstudio.com) and install our [Slint extension](https://marketplace.visualstudio.com/items?itemName=Slint.slint).

1. Install [uv](https://docs.astral.sh/uv/)
2. Download and extract the [ZIP archive of this repository](https://github.com/slint-ui/material-python-template/archive/refs/heads/master.zip).
3. Rename the extracted directory and change into it:
    ```sh
    mv material-python-template-master my-project
    cd my-project
    ```

## Run your application on desktop

1. Run the application:

    ```
    uv run main.py
    ```

## Next Steps

We hope that this template helps you get started, and that you enjoy exploring making user interfaces with Slint. To learn more
about the Slint APIs and the `.slint` markup language, check out our [online documentation](https://slint.dev/docs). Check out
also the [material components documentation](https://material.slint.dev/overview/)
