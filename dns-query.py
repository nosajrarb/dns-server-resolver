from dataclasses import dataclass
import dataclasses
import struct
import random 

@dataclass
class DNSHeader:
    id: int
    flags: int
    #counts 
    num_questions: int = 0
    num_answers: int = 0
    num_authorities: int = 0
    num_additionals: int = 0
    
@dataclass
class DNSQuestion:
    name: bytes
    type_: int
    class_: int
    
    
def header_to_bytes(header):
    fields = dataclasses.astuple(header)
    return struct.pack('!HHHHHH',*fields)

def question_to_bytes(question):
    return question.name + struct.pack('!HH', question.type_, question.class_)

def encode_dns_name(domain_name):
    encoded = b""
    for part in domain_name.encode("ascii").split(b"."):
        encoded += bytes([len(part)]) + part
    return encoded + b"\x00"

x =encode_dns_name("google.com")
print(x)
