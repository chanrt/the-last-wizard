from states import *
from object import Object


def load(objects):
    objects.append(Object(0, 0, Objects.large_rock))
    objects.append(Object(1, 0, Objects.road))
    objects.append(Object(1.1, 0.1, Objects.road))
    objects.append(Object(1.2, 0.2, Objects.road))
    objects.append(Object(1.3, 0.3, Objects.road))
    objects.append(Object(1.4, 0.4, Objects.road))
