import json
import time
import typing as t

import boto3
from rich.console import Console
from rich.live import Live
from rich.tree import Tree

if t.TYPE_CHECKING:
    from mypy_boto3_sqs import SQSClient

sqs: "SQSClient" = boto3.client("sqs", endpoint_url="http://localhost:4566")
messages: "SQSClient" = boto3.client(
    "sqs",
    endpoint_url="http://localhost:4566/_aws/sqs/messages?ShowDelayed=true&ShowInvisible=true",
)


def generate_tree() -> Tree:
    tree = Tree("Queues")

    queue_urls = sqs.list_queues().get("QueueUrls", [])

    for queue_url in queue_urls:
        message_list = messages.receive_message(QueueUrl=queue_url).get("Messages", [])

        queue_tree = tree.add(f"📂 [blue][b]{queue_url}[/b][/blue]")

        for message in message_list:
            if message["Attributes"]["IsDelayed"] == "true":
                prefix = "🐌"
            elif message["Attributes"]["IsVisible"] == "false":
                prefix = "📨 "
            else:
                prefix = "✉️ "

            message_tree = queue_tree.add(f"{prefix} {message['MessageId']}")

            message_body = message_tree.add(f"Body")
            try:
                body_str = json.dumps(json.loads(message["Body"]))
            except:
                body_str = message["Body"]

            message_body.add(body_str)
            attributes = message_tree.add(f"Attributes")
            attributes.add(f"MD5OfBody: {message['MD5OfBody']}")

            for k, v in message["Attributes"].items():
                attributes.add(f"{k}: {v}")

    return tree


def main():
    console = Console()

    with Live(console=console, screen=True, auto_refresh=False) as live:
        try:
            while True:
                live.update(generate_tree(), refresh=True)
                time.sleep(1)
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
