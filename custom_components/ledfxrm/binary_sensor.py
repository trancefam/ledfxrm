"""Binary sensor platform for ledfxrm."""
from homeassistant.components.binary_sensor import BinarySensorDevice

from custom_components.ledfxrm.const import (
    BINARY_SENSOR,
    BINARY_SENSOR_DEVICE_CLASS,
    DEFAULT_NAME,
    DOMAIN,
)
from custom_components.ledfxrm.entity import LedfxrmEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([LedfxrmBinarySensor(coordinator, entry)])


class LedfxrmBinarySensor(LedfxrmEntity, BinarySensorDevice):
    """ledfxrm binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("bool_on", False)