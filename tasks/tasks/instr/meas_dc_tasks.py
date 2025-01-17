# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2018 by ExopyHqcLegacy Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Task to measure DC properties.

"""
from time import sleep

from atom.api import Float, set_default

from exopy.tasks.api import InstrumentTask


class MeasDCVoltageTask(InstrumentTask):
    """Measure a dc voltage.

    Wait for any parallel operation before execution and then wait the
    specified time before perfoming the measure.

    """
    # Time to wait before the measurement.
    wait_time = Float().tag(pref=True)

    database_entries = set_default({'voltage': 1.0})

    wait = set_default({'activated': True, 'wait': ['instr']})

    def perform(self):
        """Wait and read the DC voltage.

        """
        sleep(self.wait_time)

        value = self.driver.read_voltage_dc()
        self.write_in_database('voltageDC', value)
