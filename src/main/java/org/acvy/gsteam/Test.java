package org.acvy.gsteam;

import org.springframework.context.support.ClassPathXmlApplicationContext;


public class Test {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("appContext.xml");

        Music music = context.getBean("rockMusic", Music.class);
        MusicPlayer player = new MusicPlayer(music);
        player.play();
    }
}
