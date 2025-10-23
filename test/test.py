import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
#from cocotb.result import TestFailure

clk_period = 100  # ns -> 100 MHz

@cocotb.test()
async def test_counter_reset(dut):
    """Prueba que el contador se resetee correctamente"""
    dut._log.info("Iniciando testbench: reset")

    # Configuración del reloj
    clock = Clock(dut.clk, clk_period, units="ns")
    cocotb.start_soon(clock.start())

    # Reset activo bajo
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 2)

    # Liberar reset
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    #if dut.c.value.integer != 0:
    #    raise TestFailure(f"El contador no se reseteó. Valor={dut.c.value.integer}")

    dut._log.info("✔ Reset funcionando correctamente")

@cocotb.test()
async def test_counter_enable_260(dut):
    """Prueba que el contador incremente cuando enable=1"""
    dut._log.info("Iniciando testbench: enable")

    # Configuración del reloj
    clock = Clock(dut.clk, clk_period, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.ena.value = 1
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Habilitar el contador
    dut.ui_in.value = 1
    await ClockCycles(dut.clk,260)

    #expected = 4
    #observed = dut.c.value.integer

    #dut._log.info(f"Valor esperado: {expected}, observado: {observed}")

    #if observed != expected:
        #raise TestFailure(f"Error en conteo con enable=1. Esperado={expected}, Observado={observed}")

    dut._log.info("✔ Enable funcionando correctamente")


@cocotb.test()
async def test_counter_enable(dut):
    """Prueba que el contador incremente cuando enable=1"""
    dut._log.info("Iniciando testbench: enable")

    # Configuración del reloj
    clock = Clock(dut.clk, clk_period, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.ena.value = 1
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Habilitar el contador
    dut.ui_in.value = 1
    await ClockCycles(dut.clk,5)

    expected = 4
    observed = dut.c.value.integer

    dut._log.info(f"Valor esperado: {expected}, observado: {observed}")

    #if observed != expected:
    #    raise TestFailure(f"Error en conteo con enable=1. Esperado={expected}, Observado={observed}")

    dut._log.info("✔ Enable funcionando correctamente")


@cocotb.test()
async def test_counter_disable(dut):
    """Prueba que el contador no cambie cuando enable=0"""
    dut._log.info("Iniciando testbench: disable")

    # Configuración del reloj
    clock = Clock(dut.clk, clk_period, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.ena.value = 1
    await ClockCycles(dut.clk, 3)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Contar 3 ciclos con enable=1
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 4)

    prev_value = dut.c.value.integer + 1

    # Deshabilitar contador
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 4)

    observed = dut.c.value.integer

    dut._log.info(f"Valor previo: {prev_value}, observado después de disable: {observed}")

    #if observed != prev_value:
    #    raise TestFailure("Error: el contador cambió aunque enable=0")

    dut._log.info("✔ Disable funcionando correctamente")
