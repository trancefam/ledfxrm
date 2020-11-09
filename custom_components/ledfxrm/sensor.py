"""Sensor platform for ledfxrm."""
from custom_components.ledfxrm.const import DEFAULT_NAME, DOMAIN, ICON_STRIP, SENSOR
from custom_components.ledfxrm.entity import LedfxrmEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([LedfxrmSensor(coordinator, entry)])


class LedfxrmSensor(LedfxrmEntity):
    """ledfxrm Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("static")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON_STRIP