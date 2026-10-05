import random
import string

class Codec:
    def __init__(self):
        # Character set for Base62 encoding: 26 lowercase + 26 uppercase + 10 digits = 62 characters
        self.chars = string.ascii_letters + string.digits
        self.code_length = 6
        self.base_url = "http://tinyurl.com/"
        
        # Bi-directional mapping to ensure idempotence and fast lookups
        self.url_to_code = {}
        self.code_to_url = {}

    def _generate_code(self) -> str:
        """Generates a random 6-character Base62 alphanumeric string."""
        return ''.join(random.choices(self.chars, k=self.code_length))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # If the URL is already shortened, return the existing tiny URL (idempotency)
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate a unique 6-character code, handling collisions
        code = self._generate_code()
        while code in self.code_to_url:
            code = self._generate_code()
            
        # Store bi-directional mappings
        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code
        
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # Extract the 6-character key from the end of the URL
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
