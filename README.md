# UDPReceiver
Sample application to demonstrate reception of encoded UDP messages in Python. Currently, it only supports timestamps

## Protocol
The current protocol is very simple since it only supports a single message type. The first byte of the packet indicates the message type (only `0x01` is valid, for timestamps). The rest of the packet is the payload. Timestamps must be encoded as big-endian 8-byte longs (long longs).

## Requirements
Python 3

## Running
`python3 udpReceiver.py`

If you want to receive messages broadcast from another machine, you will probably need to modify the `host` variable to match the IP address of the listening machine's interface (that is, the network IP address of the computer running this code). Likewise, the machine broadcasting will need to broadcast to that IP.