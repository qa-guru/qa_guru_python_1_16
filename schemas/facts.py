from voluptuous import ALLOW_EXTRA
from voluptuous import Schema

fact = Schema({
    'fact': str,
    "length": int
})

facts = Schema(
    {
        "data": [fact]
    },
    extra=ALLOW_EXTRA,
    required=True
)
