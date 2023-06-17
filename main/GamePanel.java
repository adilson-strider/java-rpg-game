package main;

import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JPanel;

public class GamePanel extends JPanel implements Runnable{

    final int originalTileSize = 16;
    final int scale = 3;
    final int tileSize = originalTileSize * scale;
    final int maxScreenColumn = 16;
    final int maxScreenRow = 12;
    final int screenWidth = maxScreenColumn * tileSize;
    final int screeHeight = maxScreenRow * tileSize;

    Thread thread;
    
    public GamePanel(){
        this.setPreferredSize(new Dimension(screenWidth, screeHeight));
        this.setBackground(new Color(100, 149, 237));
        this.setDoubleBuffered(true);
    }

    @Override
    public void run() {
        
        while (thread != null) {
            System.out.println("Rodando!");
        }
    }

    public void startGameThread(){
        thread = new Thread(this);
        thread.start();
    }
}
