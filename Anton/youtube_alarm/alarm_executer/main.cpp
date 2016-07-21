/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: zapolsky
 *
 * Created on 21 июля 2016 г., 14:14
 */

#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    string command = "python ";
    string filename = "d:\\Study\\Python\\sc-python\\Anton\\youtube_alarm\\alarm.py";
    string call_python_command = command + filename;
    system(call_python_command.c_str());
    return 0;
}

