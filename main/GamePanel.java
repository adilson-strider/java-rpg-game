package main;

import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JPanel;

public class GamePanel extends JPanel{

    final int originalTileSize = 16;
    final int scale = 3;
    final int tileSize = originalTileSize * scale;
    final int maxScreenColumn = 16;
    final int maxScreenRow = 12;
    final int screenWidth = maxScreenColumn * tileSize;
    final int screeHeight = maxScreenRow * tileSize;
    
    public GamePanel(){
        this.setPreferredSize(new Dimension(screenWidth, screeHeight));
        this.setBackground(new Color(100, 149, 237));
        this.setDoubleBuffered(true);
    }
}
