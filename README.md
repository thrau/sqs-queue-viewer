SQS Queue Viewer
===============================

SQS Queue Viewer for LocalStack.
Shows a tree of queues and their messages.
Uses LocalStack's internal [SQS developer endpoints](https://docs.localstack.cloud/user-guide/aws/sqs/#developer-endpoints).


## Quickstart

to install the python and other developer requirements into a venv run:

    make install

## Use

Start LocalStack and run

    .venv/bin/python -m sqs_queue_viewer

It creates a live-updating view, press CTRL+C to quit.

Example output:

```console
Queues
├── 📂 http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/input-dead-letter-queue
├── 📂 http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/input-queue
└── 📂 http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/recovery-queue
    ├── ✉️  626e84a0-5e11-4e2b-a177-20b8e7f26db4
    │   ├── Body
    │   │   └── {"hello": "world 1
    │   └── Attributes
    │       ├── MD5OfBody: f1f63041157297d726dba6b6a9c9e8bf
    │       ├── ApproximateReceiveCount: 0
    │       ├── ApproximateFirstReceiveTimestamp: 0
    │       ├── IsVisible: true
    │       └── IsDelayed: false
    └── ✉️  4167f289-2805-42b6-a1f7-d2ea80e927b6
        ├── Body
        │   └── {"hello": "world 2
        └── Attributes
            ├── MD5OfBody: 88747add4febf291266947763678bc6e
            ├── ApproximateReceiveCount: 0
            ├── ApproximateFirstReceiveTimestamp: 0
            ├── IsVisible: true
            └── IsDelayed: false
```
