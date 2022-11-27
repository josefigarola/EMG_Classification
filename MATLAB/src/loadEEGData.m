function [eegData] = loadEEGData(fileName)
% loadEEGData loads an EEG file in memory.
% This function loads an EEG file and returns a structure that 
% contains the loaded data.
%
%   - Parameters: fileName - File path.
%
%   - Outputs: eegData - Structure with the loaded data.
%
%   Author: Omar Mendoza Montoya
%  5

% Check input arguments.
if nargin ~= 1
    error('Wrong number of input arguments.')
end

% Open file.
fid = fopen(fileName);

% Read magic key.
magic = strtrim(fgets(fid));
if (~strcmpi(magic, 'ebr binary 1.0'))
    error('Unknown file format.')
end

% Build basic elements of the structure.
eegData.ns = 0;     % Number of samples per sequence.
eegData.nb = 0;     % Number of bands.
eegData.nc = 0;     % Number of channels.
eegData.nt = 0;     % Number of trials.
eegData.nmarks = 0;     % Number of marks.
eegData.ncomments = 0;  % Number of comments.
eegData.sampRate = 0;           % Sampling rate.
eegData.dataType = 'Unknown';   % Data type.

eegData.bands = cell(eegData.nb, 1);
eegData.channels = cell(eegData.nc, 1);
eegData.trials = cell(eegData.nt, 1);
eegData.comments = cell(eegData.ncomments, 1);
eegData.marks = cell(eegData.nmarks, 1);
eegData.markpositions = zeros(eegData.nmarks, 1);

% Read line by line of the header.
endHeader = false;
while(~endHeader)
    line = fgets(fid);
    [itemName, itemValue] = strtok(strtrim(line)); 
    
    itemName = lower(strtrim(itemName));
    itemValue = lower(strtrim(itemValue));
    
    if strcmpi(itemName, 'data_type')
        eegData.dataType = itemValue;
        
    elseif strcmpi(itemName, 'sampling_rate')
        [eegData.sampRate, status] = str2num(itemValue);
        if (~status)
            error('Wrong sampling rate.')
        end
        
    elseif strcmpi(itemName, 'samples')
        [eegData.ns, status] = str2num(itemValue);
        if (~status)
            error('Wrong number of samples.')
        end
        
    elseif strcmpi(itemName, 'bands')
        [eegData.nb, status] = str2num(itemValue);
        if (~status)
            error('Wrong number of bands.')
        end
        eegData.bands = cell(eegData.nb, 1);
        
    elseif strcmpi(itemName, 'channels')
        [eegData.nc, status] = str2num(itemValue);
        if (~status)
            error('Wrong number of channels.')
        end
        eegData.channels = cell(eegData.nc, 1);
        
    elseif strcmpi(itemName, 'trials')
        [eegData.nt, status] = str2num(itemValue);
        if (~status)
            error('Wrong number of trials.')
        end
        eegData.trials = cell(eegData.nt, 1);
        
    elseif strcmpi(itemName, 'comments')
        [eegData.ncomments, status] = str2num(itemValue);
        if (~status)
            error('Wrong number of comments.')
        end
        eegData.comments = cell(eegData.ncomments, 1);
        
    elseif strcmpi(itemName, 'marks')
        [eegData.nmarks, status] = str2num(itemValue);
        if (~status)
            error('Wrong number of marks.')
        end
        eegData.marks = cell(eegData.nmarks, 1);
        eegData.markpositions = zeros(eegData.nmarks, 1);
        
    elseif strcmpi(itemName, 'end_header')
        
        nmov = length(line) - 11;
        if (nmov ~= 0)
            fseek(fid, -nmov, 0)
        end
        endHeader = true;    
        
    elseif (length(itemName) > 5) && strcmpi(itemName(1:5), 'band_')
       [index, status] = str2num(itemName(6:length(itemName)));
        if (~status)
            error('Wrong band index.')
        end
        
        eegData.bands(index) = cellstr(itemValue);
        
    elseif (length(itemName) > 8) && strcmpi(itemName(1:8), 'channel_')
        [index, status] = str2num(itemName(9:length(itemName)));
        if (~status)
            error('Wrong channel index.')
        end
        
        eegData.channels(index) = cellstr(itemValue);
        
    elseif (length(itemName) > 6) && strcmpi(itemName(1:6), 'trial_')
        [index, status] = str2num(itemName(7:length(itemName)));
        if (~status)
            error('Wrong trial index.')
        end
        
        eegData.trials(index) = cellstr(itemValue);
    
    elseif (length(itemName) > 8) && strcmpi(itemName(1:8), 'comment_')
        index = str2num(itemName(9:length(itemName)));
        if (~status)
            error('Wrong comment index.')
        end
        
        eegData.comments(index) = cellstr(itemValue);
      
    elseif (length(itemName) > 5) && strcmpi(itemName(1:5), 'mark_')
        [index, status] = str2num(itemName(6:length(itemName)));
        if (~status)
            error('Wrong mark index.')
        end
        [pos, mark] = strtok(itemValue);         
        [pos, status] = str2num(pos);
        if (~status)
            error('Wrong position index.')
        end
        
        eegData.marks(index) = cellstr(strtrim(mark));
        eegData.markpositions(index) = pos;
        
    else 
        error('Unknown item in file.')
    end
      
end

% Read data section.
size = eegData.ns*eegData.nb*eegData.nc*eegData.nt;
switch eegData.dataType
    case 'int8'
        eegData.data = fread(fid, size, 'int8');
        
    case 'char'
        eegData.data = fread(fid, size, 'int8');
        
    case 'int16'
        eegData.data = fread(fid, size, 'int16');
    
    case 'short'
        eegData.data = fread(fid, size, 'int16');
        
    case 'int32'
        eegData.data = fread(fid, size, 'int32');
    
    case 'int'
        eegData.data = fread(fid, size, 'int32');
        
    case 'int64'
        eegData.data = fread(fid, size, 'int64');
        
   case 'long long'
        eegData.data = fread(fid, size, 'int64');
        
    case 'uint8'
        eegData.data = fread(fid, size, 'uint8');
    
    case 'unsigned char'
        eegData.data = fread(fid, size, 'uint8');
        
    case 'uint16'
        eegData.data = fread(fid, size, 'uint16');
    
    case 'unsigned short'
        eegData.data = fread(fid, size, 'uint16');
        
    case 'uint32'
        eegData.data = fread(fid, size, 'uint32');
    
    case 'unsigned int'
        eegData.data = fread(fid, size, 'uint32');
        
    case 'uint64'
        eegData.data = fread(fid, size, 'uint64');
    
    case 'unsigned long long'
        eegData.data = fread(fid, size, 'uint64');
        
    case 'float' 
        eegData.data = fread(fid, size, 'float32');
        
    case 'double'  
        eegData.data = fread(fid, size, 'float64');
        
    case 'complex'  
        complexData = fread(fid, size*2, 'float64');
        eegData.data = complexData(1:2:length(complexData)) + 1i*complexData(2:2:length(complexData));
        
    case 'class std::complex<double>'
        complexData = fread(fid, size*2, 'float64');
        eegData.data = complexData(1:2:length(complexData)) + 1i*complexData(2:2:length(complexData));
        
    otherwise
      error('Unknown data type.');
end

eegData.data= reshape(eegData.data, eegData.ns, eegData.nb, eegData.nc, eegData.nt);

% close file.
fclose(fid);

end
