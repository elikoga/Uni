----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06/08/2022 03:49:10 PM
-- Design Name: 
-- Module Name: stopwatch - Behavioral
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

ENTITY stopwatch IS
    PORT (
        clk100mhz : IN STD_LOGIC;
        start : IN STD_LOGIC;
        stop : IN STD_LOGIC;
        pause : IN STD_LOGIC;
        an_n : OUT STD_LOGIC_VECTOR (7 DOWNTO 0);
        leds_n : OUT STD_LOGIC_VECTOR (6 DOWNTO 0));
END stopwatch;

ARCHITECTURE Behavioral OF stopwatch IS

    COMPONENT segmentctrl IS
        PORT (
            clk100mhz : IN STD_LOGIC;
            digit_0 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
            digit_1 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
            digit_2 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
            digit_3 : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
            an_n : OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
            leds_n : OUT STD_LOGIC_VECTOR(6 DOWNTO 0));
    END COMPONENT;

    COMPONENT tick_generator IS -- actually a divider
        PORT (
            clk100mhz : IN STD_LOGIC;
            tick : OUT STD_LOGIC;
            divider : IN STD_LOGIC_VECTOR (31 DOWNTO 0);
            en : IN STD_LOGIC);
    END COMPONENT;

    COMPONENT counter IS
        PORT (
            tick_in : IN STD_LOGIC;
            rst : IN STD_LOGIC;
            max_count : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
            digit_out : OUT STD_LOGIC_VECTOR (3 DOWNTO 0);
            tick_out : OUT STD_LOGIC);
    END COMPONENT;

    COMPONENT state_machine IS
        PORT (
            clk100mhz : IN STD_LOGIC;
            start : IN STD_LOGIC;
            stop : IN STD_LOGIC;
            pause : IN STD_LOGIC;
            en : OUT STD_LOGIC;
            rst : OUT STD_LOGIC);
    END COMPONENT;

    SIGNAL en : STD_LOGIC;
    SIGNAL rst : STD_LOGIC;
    SIGNAL tick : STD_LOGIC;

    SIGNAL digit_0 : STD_LOGIC_VECTOR (3 DOWNTO 0);
    SIGNAL digit_1 : STD_LOGIC_VECTOR (3 DOWNTO 0);
    SIGNAL digit_2 : STD_LOGIC_VECTOR (3 DOWNTO 0);
    SIGNAL digit_3 : STD_LOGIC_VECTOR (3 DOWNTO 0);

    SIGNAL tick_s0 : STD_LOGIC;
    SIGNAL tick_s1 : STD_LOGIC;
    SIGNAL tick_m0 : STD_LOGIC;
BEGIN
    SEGMENT_CTRL : segmentctrl PORT MAP(
        clk100mhz => clk100mhz,
        digit_0 => digit_0,
        digit_1 => digit_1,
        digit_2 => digit_2,
        digit_3 => digit_3,
        an_n => an_n,
        leds_n => leds_n);

    TICK_GENERATOR_0 : tick_generator PORT MAP(
        clk100mhz => clk100mhz,
        tick => tick,
        divider => STD_LOGIC_VECTOR(to_unsigned(100000000, 32)), -- 1s * 100mHz = 100_000_000
        en => en);

    COUNTER_s0 : counter PORT MAP(
        tick_in => tick,
        rst => rst,
        max_count => STD_LOGIC_VECTOR(to_unsigned(9, 4)),
        digit_out => digit_0,
        tick_out => tick_s0);

    COUNTER_s1 : counter PORT MAP(
        tick_in => tick_s0,
        rst => rst,
        max_count => STD_LOGIC_VECTOR(to_unsigned(5, 4)),
        digit_out => digit_1,
        tick_out => tick_s1);

    COUNTER_m0 : counter PORT MAP(
        tick_in => tick_s1,
        rst => rst,
        max_count => STD_LOGIC_VECTOR(to_unsigned(9, 4)),
        digit_out => digit_2,
        tick_out => tick_m0);

    COUNTER_m1 : counter PORT MAP(
        tick_in => tick_m0,
        rst => rst,
        max_count => STD_LOGIC_VECTOR(to_unsigned(9, 4)),
        digit_out => digit_3,
        tick_out => OPEN);

    STATE_MACHINE_0 : state_machine PORT MAP(
        clk100mhz => clk100mhz,
        start => start,
        stop => stop,
        pause => pause,
        en => en,
        rst => rst);

END Behavioral;