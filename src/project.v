/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out  = ui_in + uio_in;  // Example: ou_out is the sum of ui_in and uio_in
  assign uio_out = 0;
  assign uio_oe  = 0;// All output pins must be assigned. If not used, assign to 0.
  assign uio_oe  = 8'b1000_0000;  // Set all IOs as inputs
  assign uio_out[6:0] = 7'b000_0000;  // Drive outputs to 0 when not used
  wire enable;
  wire [7:0] c;
  wire cout;
  assign enable = ui_in[0];  // Example: ou_out is the sum of ui_in and uio_in
  assign uo_out[7:0] = c;
  assign uio_out[7] = cout;
  SUMADOR8BITS SUMADOR8BITS_Unit(
        .clk(clk),
        .rst(rst_n),
        .enable(enable), 
        .c(c),
        .cout(cout)
    );

// List all unused inputs to prevent warnings
wire _unused = &{ena, uio_in[7:0],  ui_in[7:1], 1'b0};//uio_out[6:0],



endmodule
