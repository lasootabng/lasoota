import json
import redis
# from datetime import timedelta

r = redis.Redis(host="localhost", port=6379, db=0)

PENDING_TTL_SECONDS = 10 * 60  # 10 minutes

def save_pending_signup(signup_id: str, data: dict):
    key = f"pending_signup:{signup_id}"
    r.setex(key, PENDING_TTL_SECONDS, json.dumps(data))

def get_pending_signup(signup_id: str):
    key = f"pending_signup:{signup_id}"
    raw = r.get(key)
    if not raw:
        return None
    return json.loads(raw)

def delete_pending_signup(signup_id: str):
    key = f"pending_signup:{signup_id}"
    r.delete(key)


if __name__ == '__main__':
    save_pending_signup(1, '{"sample": "bipul"}')
    print(get_pending_signup(1))