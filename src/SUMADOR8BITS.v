module SUMADOR8BITS(
	input wire clk,
	input wire rst,
	input wire enable,
	output reg [7:0] c,
	output reg cout
);

	always@(posedge clk or negedge rst) begin
		if(!rst)
		begin
			c = 8'd0;
			cout=1'b0;
		end
		else if(enable)
			{cout,c} = {cout,c} + 9'd1;
	end
endmodule
