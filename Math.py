import math

def angle_between(v1, v2):
    dot_product =  v1.dot(v2)
    magnitudes = v1.length() * v2.length()
    if magnitudes != 0:
        cosine_angle = max(min(dot_product/magnitudes,1),-1)
        return math.acos(cosine_angle)
    return None
