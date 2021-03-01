using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 上传代码生成器
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void player1_big_winner_CheckedChanged(object sender, EventArgs e)
        {
            player2_big_winner.Enabled = !player2_big_winner.Enabled;
            player3_big_winner.Enabled = !player3_big_winner.Enabled;
            player4_big_winner.Enabled = !player4_big_winner.Enabled;
        }

        private void player2_big_winner_CheckedChanged(object sender, EventArgs e)
        {
            player1_big_winner.Enabled = !player1_big_winner.Enabled;
            player3_big_winner.Enabled = !player3_big_winner.Enabled;
            player4_big_winner.Enabled = !player4_big_winner.Enabled;
        }

        private void player3_big_winner_CheckedChanged(object sender, EventArgs e)
        {
            player1_big_winner.Enabled = !player1_big_winner.Enabled;
            player2_big_winner.Enabled = !player2_big_winner.Enabled;
            player4_big_winner.Enabled = !player4_big_winner.Enabled;
        }

        private void player4_big_winner_CheckedChanged(object sender, EventArgs e)
        {
            player1_big_winner.Enabled = !player1_big_winner.Enabled;
            player2_big_winner.Enabled = !player2_big_winner.Enabled;
            player3_big_winner.Enabled = !player3_big_winner.Enabled;
        }

        private void player1_big_boomer_CheckedChanged(object sender, EventArgs e)
        {
            player2_big_boomer.Enabled = !player2_big_boomer.Enabled;
            player3_big_boomer.Enabled = !player3_big_boomer.Enabled;
            player4_big_boomer.Enabled = !player4_big_boomer.Enabled;
        }

        private void player2_big_boomer_CheckedChanged(object sender, EventArgs e)
        {
            player1_big_boomer.Enabled = !player1_big_boomer.Enabled;
            player3_big_boomer.Enabled = !player3_big_boomer.Enabled;
            player4_big_boomer.Enabled = !player4_big_boomer.Enabled;
        }

        private void player3_big_boomer_CheckedChanged(object sender, EventArgs e)
        {
            player1_big_boomer.Enabled = !player1_big_boomer.Enabled;
            player2_big_boomer.Enabled = !player2_big_boomer.Enabled;
            player4_big_boomer.Enabled = !player4_big_boomer.Enabled;
        }

        private void player4_big_boomer_CheckedChanged(object sender, EventArgs e)
        {
            player1_big_boomer.Enabled = !player1_big_boomer.Enabled;
            player2_big_boomer.Enabled = !player2_big_boomer.Enabled;
            player3_big_boomer.Enabled = !player3_big_boomer.Enabled;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 检查id是否有空白
            if (player1_id.SelectedItem is null)
            {
                MessageBox.Show("player1_id未选择，请检查！");
                return;
            }
            if (player2_id.SelectedItem is null)
            {
                MessageBox.Show("player2_id未选择，请检查！");
                return;
            }
            if (player3_id.SelectedItem is null)
            {
                MessageBox.Show("player3_id未选择，请检查！");
                return;
            }
            if (player4_id.SelectedItem is null)
            {
                MessageBox.Show("player4_id未选择，请检查！");
                return;
            }
            // 检查是否有重复id
            if (player1_id.SelectedItem.ToString() == player2_id.SelectedItem.ToString() ||
                player1_id.SelectedItem.ToString() == player3_id.SelectedItem.ToString() ||
                player1_id.SelectedItem.ToString() == player4_id.SelectedItem.ToString() ||
                player2_id.SelectedItem.ToString() == player3_id.SelectedItem.ToString() ||
                player2_id.SelectedItem.ToString() == player4_id.SelectedItem.ToString() ||
                player3_id.SelectedItem.ToString() == player4_id.SelectedItem.ToString())
            {
                MessageBox.Show("id有重复，请检查！");
                return;
            }
            // 检查score是否有空白
            if (player1_score.Text == "")
            {
                MessageBox.Show("player1_score为空，请检查！");
                return;
            }
            if (player2_score.Text == "")
            {
                MessageBox.Show("player2_score为空，请检查！");
                return;
            }
            if (player3_score.Text == "")
            {
                MessageBox.Show("player3_score为空，请检查！");
                return;
            }
            if (player4_score.Text == "")
            {
                MessageBox.Show("player4_score为空，请检查！");
                return;
            }
            // 检查hu是否有空白
            if (player1_hu.Text == "")
            {
                MessageBox.Show("player1_hu为空，请检查！");
                return;
            }
            if (player2_hu.Text == "")
            {
                MessageBox.Show("player2_hu为空，请检查！");
                return;
            }
            if (player3_hu.Text == "")
            {
                MessageBox.Show("player3_hu为空，请检查！");
                return;
            }
            if (player4_hu.Text == "")
            {
                MessageBox.Show("player4_hu为空，请检查！");
                return;
            }
            // 检查zhuang是否有空白
            if (player1_zhuang.Text == "")
            {
                MessageBox.Show("player1_zhuang为空，请检查！");
                return;
            }
            if (player2_zhuang.Text == "")
            {
                MessageBox.Show("player2_zhuang为空，请检查！");
                return;
            }
            if (player3_zhuang.Text == "")
            {
                MessageBox.Show("player3_zhuang为空，请检查！");
                return;
            }
            if (player4_zhuang.Text == "")
            {
                MessageBox.Show("player4_zhuang为空，请检查！");
                return;
            }
            // 检查pao是否有空白
            if (player1_pao.Text == "")
            {
                MessageBox.Show("player1_pao为空，请检查！");
                return;
            }
            if (player2_pao.Text == "")
            {
                MessageBox.Show("player2_pao为空，请检查！");
                return;
            }
            if (player3_pao.Text == "")
            {
                MessageBox.Show("player3_pao为空，请检查！");
                return;
            }
            if (player4_pao.Text == "")
            {
                MessageBox.Show("player4_pao为空，请检查！");
                return;
            }
            // 检查bao是否有空白
            if (player1_bao.Text == "")
            {
                MessageBox.Show("player1_bao为空，请检查！");
                return;
            }
            if (player2_bao.Text == "")
            {
                MessageBox.Show("player2_bao为空，请检查！");
                return;
            }
            if (player3_bao.Text == "")
            {
                MessageBox.Show("player3_bao为空，请检查！");
                return;
            }
            if (player4_bao.Text == "")
            {
                MessageBox.Show("player4_bao为空，请检查！");
                return;
            }
            // 检查lou是否有空白
            if (player1_lou.Text == "")
            {
                MessageBox.Show("player1_lou为空，请检查！");
                return;
            }
            if (player2_lou.Text == "")
            {
                MessageBox.Show("player2_lou为空，请检查！");
                return;
            }
            if (player3_lou.Text == "")
            {
                MessageBox.Show("player3_lou为空，请检查！");
                return;
            }
            if (player4_lou.Text == "")
            {
                MessageBox.Show("player4_lou为空，请检查！");
                return;
            }
            // 检查大赢家勾选是否空白
            if (!(player1_big_winner.Checked || player2_big_winner.Checked || player3_big_winner.Checked || player4_big_winner.Checked))
            {
                MessageBox.Show("大赢家未勾选，请检查！");
                return;
            }
            // 检查最佳炮手勾选是否空白
            if (!(player1_big_boomer.Checked || player2_big_boomer.Checked || player3_big_boomer.Checked || player4_big_boomer.Checked))
            {
                MessageBox.Show("最佳炮手未勾选，请检查！");
                return;
            }
            // 检查积分和是否为0
            if (int.Parse(player1_score.Text) + int.Parse(player2_score.Text) + int.Parse(player3_score.Text) + int.Parse(player4_score.Text) != 0)
            {
                MessageBox.Show("积分和不为0，请检查！");
                return;
            }

            string result = "upload-" +
                player1_id.SelectedItem.ToString() + "," + player1_score.Text + "," +
                player1_hu.Text + "," + player1_zhuang.Text + "," + player1_pao.Text + "," + player1_bao.Text + "," + player1_lou.Text + "," +
                (player1_big_winner.Checked ? "1" : "0") + "," + (player1_big_boomer.Checked ? "1" : "0") + ";" +

                player2_id.SelectedItem.ToString() + "," + player2_score.Text + "," +
                player2_hu.Text + "," + player2_zhuang.Text + "," + player2_pao.Text + "," + player2_bao.Text + "," + player2_lou.Text + "," +
                (player2_big_winner.Checked ? "1" : "0") + "," + (player2_big_boomer.Checked ? "1" : "0") + ";" +

                player3_id.SelectedItem.ToString() + "," + player3_score.Text + "," +
                player3_hu.Text + "," + player3_zhuang.Text + "," + player3_pao.Text + "," + player3_bao.Text + "," + player3_lou.Text + "," +
                (player3_big_winner.Checked ? "1" : "0") + "," + (player3_big_boomer.Checked ? "1" : "0") + ";" +

                player4_id.SelectedItem.ToString() + "," + player4_score.Text + "," +
                player4_hu.Text + "," + player4_zhuang.Text + "," + player4_pao.Text + "," + player4_bao.Text + "," + player4_lou.Text + "," +
                (player4_big_winner.Checked ? "1" : "0") + "," + (player4_big_boomer.Checked ? "1" : "0");

            upload_code.Text = result;
            MessageBox.Show("代码生成成功！");
            return;
        }

        private void copy_Click(object sender, EventArgs e)
        {
            if (upload_code.Text == "")
            {
                MessageBox.Show("代码框为空，复制失败！");
                return;
            }
            Clipboard.SetDataObject(upload_code.Text);
            MessageBox.Show("复制成功！");
            return;
        }

        private void clear_button_Click(object sender, EventArgs e)
        {
            player1_id.Text = "";
            player1_score.Text = "";
            player1_hu.Text = "";
            player1_zhuang.Text = "";
            player1_pao.Text = "";
            player1_bao.Text = "";
            player1_lou.Text = "";

            player2_id.Text = "";
            player2_score.Text = "";
            player2_hu.Text = "";
            player2_zhuang.Text = "";
            player2_pao.Text = "";
            player2_bao.Text = "";
            player2_lou.Text = "";

            player3_id.Text = "";
            player3_score.Text = "";
            player3_hu.Text = "";
            player3_zhuang.Text = "";
            player3_pao.Text = "";
            player3_bao.Text = "";
            player3_lou.Text = "";

            player4_id.Text = "";
            player4_score.Text = "";
            player4_hu.Text = "";
            player4_zhuang.Text = "";
            player4_pao.Text = "";
            player4_bao.Text = "";
            player4_lou.Text = "";

            player1_big_winner.Checked = false;
            player2_big_winner.Checked = false;
            player3_big_winner.Checked = false;
            player4_big_winner.Checked = false;

            player1_big_boomer.Checked = false;
            player2_big_boomer.Checked = false;
            player3_big_boomer.Checked = false;
            player4_big_boomer.Checked = false;

            upload_code.Text = "";
            return;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
