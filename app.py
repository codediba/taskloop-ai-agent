import gradio as gr
from agent import TaskLoopAgent


async def setup():
    agent = TaskLoopAgent()
    await agent.setup()
    return agent


async def process_message(agent, message, success_criteria, history):
    results = await agent.run_superstep(message, success_criteria, history)
    return results, agent


async def reset():
    new_agent = TaskLoopAgent()
    await new_agent.setup()
    return "", "", None, new_agent


def free_resources(agent):
    print("Cleaning up")
    try:
        if agent:
            agent.cleanup()
    except Exception as e:
        print(f"Exception during cleanup: {e}")


with gr.Blocks(title="TaskLoop AI Agent", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## TaskLoop AI Agent")

    agent = gr.State(delete_callback=free_resources)

    with gr.Row():
        chatbot = gr.Chatbot(label="TaskLoop Agent", height=300, type="messages")

    with gr.Group():
        with gr.Row():
            message = gr.Textbox(
                show_label=False,
                placeholder="Enter your task"
            )
        with gr.Row():
            success_criteria = gr.Textbox(
                show_label=False,
                placeholder="Define success criteria (optional)"
            )

    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Run", variant="primary")

    ui.load(setup, [], [agent])

    message.submit(
        process_message,
        [agent, message, success_criteria, chatbot],
        [chatbot, agent]
    )

    success_criteria.submit(
        process_message,
        [agent, message, success_criteria, chatbot],
        [chatbot, agent]
    )

    go_button.click(
        process_message,
        [agent, message, success_criteria, chatbot],
        [chatbot, agent]
    )

    reset_button.click(
        reset,
        [],
        [message, success_criteria, chatbot, agent]
    )


ui.launch(inbrowser=True)
