----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06/08/2022 02:26:50 PM
-- Design Name: 
-- Module Name: segmentctrl - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
USE IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

ENTITY segmentctrl IS
    PORT (
        clk100mhz : IN STD_LOGIC;
        digit_0 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
        digit_1 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
        digit_2 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
        digit_3 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
        an_n : OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
        leds_n : OUT STD_LOGIC_VECTOR(6 DOWNTO 0));
END segmentctrl;

ARCHITECTURE Behavioral OF segmentctrl IS

    COMPONENT tick_generator IS -- actually a divider
        PORT (
            clk100mhz : IN STD_LOGIC;
            tick : OUT STD_LOGIC;
            divider : IN STD_LOGIC_VECTOR (31 DOWNTO 0);
            en : IN STD_LOGIC);
    END COMPONENT;

    COMPONENT tick_counter IS
        PORT (
            tick : IN STD_LOGIC;
            an_cnt : OUT STD_LOGIC_VECTOR (1 DOWNTO 0));
    END COMPONENT;

    COMPONENT segment IS
        PORT (
            value : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
            leds_n : OUT STD_LOGIC_VECTOR(6 DOWNTO 0)
        );
    END COMPONENT;

    SIGNAL tick : STD_LOGIC;

    SIGNAL an_cnt : STD_LOGIC_VECTOR (1 DOWNTO 0);

    SIGNAL leds_0 : STD_LOGIC_VECTOR(6 DOWNTO 0);
    SIGNAL leds_1 : STD_LOGIC_VECTOR(6 DOWNTO 0);
    SIGNAL leds_2 : STD_LOGIC_VECTOR(6 DOWNTO 0);
    SIGNAL leds_3 : STD_LOGIC_VECTOR(6 DOWNTO 0);
BEGIN

    generator : tick_generator
    PORT MAP(
        clk100mhz => clk100mhz,
        tick => tick,
        divider => STD_LOGIC_VECTOR(to_unsigned(100000, 32)), -- 1ms * 100mHz = 100_000
        en => '1');

    counter : tick_counter
    PORT MAP(
        tick => tick,
        an_cnt => an_cnt);

    segment_0 : segment
    PORT MAP(
        value => digit_0,
        leds_n => leds_0);

    segment_1 : segment
    PORT MAP(
        value => digit_1,
        leds_n => leds_1);

    segment_2 : segment
    PORT MAP(
        value => digit_2,
        leds_n => leds_2);

    segment_3 : segment
    PORT MAP(
        value => digit_3,
        leds_n => leds_3);

    an_n <= -- conditionally select the correct segment
        "11111110" WHEN an_cnt(1 DOWNTO 0) = "00" ELSE
        "11111101" WHEN an_cnt(1 DOWNTO 0) = "01" ELSE
        "11111011" WHEN an_cnt(1 DOWNTO 0) = "10" ELSE
        "11110111" WHEN an_cnt(1 DOWNTO 0) = "11" ELSE
        -- don't care
        "11111111";

    leds_n <= -- conditionally select the correct segment
        leds_0 WHEN an_cnt(1 DOWNTO 0) = "00" ELSE
        leds_1 WHEN an_cnt(1 DOWNTO 0) = "01" ELSE
        leds_2 WHEN an_cnt(1 DOWNTO 0) = "10" ELSE
        leds_3 WHEN an_cnt(1 DOWNTO 0) = "11" ELSE
        -- don't care
        "1111111";
END Behavioral;