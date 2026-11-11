class Blaster:
    def fire(self):
        return 'Blasting!'

    def damage(self):
        return 50


class LaserRifle:
    def fire(self):
        return 'Laser burst!'

    def damage(self):
        return 80


weapon_factories = {
    'blaster': Blaster,
    'laser_rifle': LaserRifle,
}


def equip_officer(weapon_type: str):
    return weapon_factories.get(weapon_type.lower(), 'blaster')()
