package org.acvy.gsteam;

public class MusicPlayer {
    private Music music;

    public MusicPlayer(Music music) {
        this.music = music;
    }

    public void play() {
        System.out.println(music.getSong());
    }
}
