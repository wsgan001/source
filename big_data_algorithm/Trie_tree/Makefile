
DEBUG := y

CC = gcc

ifeq ($(DEBUG), y)
  DBG_FLAGS := -O0 -Wall -g -DDEBUG -std=c99
else
  DBG_FLAGS := -O2 -Wall -std=c99
endif

#
#  	add compile flags
#
CFLAGS += $(DBG_FLAGS)

#CFLAGS += -I$(SW_INC) -I$(USR_INC) 
#
#  the lib needed
#
LIB_FLAGS = 


#
#	 the app obj name
#
obj = trie_tree



default: $(obj)


trie_tree:trie_tree.c 
	$(CC) $(CFLAGS) -o $@  $^  $(LIB_FLAGS)

install:
	#@install -c $(obj) $(BIN_INSTALL)	

clean: 
	@rm -f *.o $(obj)
