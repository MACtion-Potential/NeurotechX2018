pause on;
CNTR = 'M09508.004.00\n';
TOPR = 'M05508.009.00\n';
TOPL = 'M11508.009.00\n';
BOTR = 'M05508.000.00\n';
BOTL = 'M11508.000.00\n';
CLAP = 'M09510.006.01\n';
still = [CNTR, CNTR];
dance = [TOPR, CNTR, TOPR, CNTR, TOPL, CNTR, TOPL, CNTR, BOTR, CNTR ,BOTR, CNTR, BOTL, CNTR, BOTL, CNTR, TOPR, CNTR, TOPL, CNTR, BOTR, CNTR, BOTL, CNTR, CLAP, CNTR, CLAP, CNTR];
danceTopR = [TOPR, CNTR];
danceBotL = [BOTL, CNTR];




messages = still;
%meArm = MeArm('COM6', 115200);
port = 'COM6';
baud = 115200;
s = serial(port, 'BaudRate', baud);
fopen(s);

pause(2);
previousTime = clock;
halt = false;
resume = false;
try
    while (true)
        if readHaltSignal()
            if (~halt)
                messages = danceTopR;
            end
            halt = true;
            resume = false;
        end
        if readResumeSignal()
            if ~resume
                messages = danceBotL;
            end
            resume = true;
            halt = false;
        end
        if (etime(clock, previousTime) > 1)
            messages(1:15);
            previousTime = clock;
            fprintf(s, messages(1:15));
            messages = [messages, messages(1:15)]
            messages(1:15) = [];
            messages;
        end
    end
catch error
    fclose(s)
    'CLOSED SERIAL'
    rethrow(error)
end

